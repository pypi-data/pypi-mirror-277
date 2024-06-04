import boto3

from genai_core.functions.retrievers.base_retriever import Retriever

from requests_aws4auth import AWS4Auth
from opensearchpy import OpenSearch, RequestsHttpConnection
from langchain.schema.document import Document
from langchain_community.embeddings import BedrockEmbeddings
from langchain_community.retrievers import TFIDFRetriever, BM25Retriever
from langchain.retrievers import EnsembleRetriever 
from langchain.schema.retriever import BaseRetriever
from langchain.callbacks.manager import CallbackManagerForRetrieverRun, AsyncCallbackManagerForRetrieverRun
from langchain_community.vectorstores import OpenSearchVectorSearch
from typing import Any, List, Dict, Tuple


class ParentRetriever(BaseRetriever): 
    """
    A retriever class for retrieving relevant documents based on a parent-child relationship from an OpenSearch index.

    Attributes:
        ensemble_retriever (BaseRetriever): The ensemble retriever used for retrieving child documents.
        client_parent: An OpenSearch client for querying parent documents.
        parent_metadata_child (str): The metadata key for the child documents.
        parent_metadata_parent (str): The metadata key for the parent documents.
    """
    ensemble_retriever:BaseRetriever 
    client_parent:OpenSearch
    index_name: str
    child_parent_key_attribute: str
    parent_metadata_child:str
    parent_metadata_parent:str
    parent_chunk_ordering:str
    
    def _get_relevant_documents(
        self, query: str,*, run_manager: CallbackManagerForRetrieverRun
    ) -> List[Document]:
        """
        Retrieves relevant documents based on a query.

        Args:
            query (str): The query string.
            run_manager (CallbackManagerForRetrieverRun): Callback manager for retriever run.
            

        Returns:
            List[Document]: A list of relevant documents.
        """
        ret_documents = self.ensemble_retriever.get_relevant_documents(query, callbacks=run_manager.get_child())
        
        ## HERE WE HAVE A TUPLE CONSISTING OF ("PARENT PARAGRAPHS": [STR/LIST], "DOC":STR)
        documents = []
        for doc in ret_documents:
            if isinstance(doc.metadata[self.parent_metadata_child], str):
                documents.append((doc.metadata[self.parent_metadata_child], doc.metadata[self.child_parent_key_attribute]))
            elif isinstance(doc.metadata[self.parent_metadata_child], list):
                for doc_ in doc.metadata[self.parent_metadata_child]:
                    documents.append((doc_, doc.metadata[self.child_parent_key_attribute]))
        documents = list(set(documents))

        results_retreiver_custom = []

        
        for document, key in documents:
            print(document, key)
            body= {
                "query": {
                    "bool": {
                        "must": [
                            {"term": {f"metadata.{self.parent_metadata_parent}.keyword": document}},
                            {"term": {f"metadata.{self.child_parent_key_attribute}.keyword": key}}
                        ]
                    }
                }
            }
            results_retreiver = self.client_parent.search(body=body, index= self.index_name)
            if len(results_retreiver["hits"]["hits"]) > 0:
                dc = results_retreiver["hits"]["hits"][0]
                text = dc["_source"]["text"]
                results_retreiver_custom.append(Document(page_content=text, metadata=dc["_source"]["metadata"]))

        ## SORT CHUNKS BASED ON A CHUNK_NUMBER
        if self.parent_chunk_ordering:
            results_retreiver_custom = sorted(results_retreiver_custom, key= lambda x: (x.metadata[self.child_parent_key_attribute], x.metadata[self.parent_chunk_ordering]))
        ##
        return results_retreiver_custom
    
    async def _aget_relevant_documents(
        self,
        query: str,
        *,
        run_manager: AsyncCallbackManagerForRetrieverRun,
        **kwargs: Any,
    ) -> List[Document]:
        raise NotImplementedError()


class OpenSearchBaseRetriever(Retriever):
    """
    A retriever class for retrieving documents from an OpenSearch index using various retrieval methods.

    Attributes:
        opensearch_address (str): The address of the OpenSearch service.
        parent_collection_name (str): The name of the parent collection.
        k_documents (int): The number of documents to retrieve.
        retrievers_list (List): A list of retriever definitions.
        parent_metadata_child (str): The metadata key for child documents.
        parent_metadata_parent (str): The metadata key for parent documents.
        child_parent_key_attribute (str): The key to link child and parent documents.
        frontend_filter_fields (Dict): The frontend filters name conversion dictionary.
        embeddings (Any): The embedding object used for retrieval.
        session: The AWS session for OpenSearch.
        credentials: The AWS credentials for OpenSearch.
        auth: The AWS4 authentication object for OpenSearch.
    """

    
    def __init__(self, **kwargs):
        self.opensearch_address = kwargs.get("opensearch_address")
        self.parent_collection_name = kwargs.get("parent_collection_name")
        self.k_documents = kwargs.get("k_documents", 3)
        self.retrievers_list = kwargs.get("retrievers_list")
        self.parent_metadata_child = kwargs.get("parent_metadata_child")
        self.parent_metadata_parent = kwargs.get("parent_metadata_parent")
        self.child_parent_key_attribute = kwargs.get("child_parent_key_attribute")
        self.frontend_filter_fields = kwargs.get("frontend_filter_fields", {})
        self.parent_chunk_ordering_metadata = kwargs.get("parent_chunk_ordering_metadata", "")
        ### Opensearch aws
        self.session = boto3.Session(region_name="eu-central-1")
        self.credentials = boto3.Session(region_name="eu-central-1").get_credentials()
        self.auth = AWS4Auth(region="eu-central-1", service='es', refreshable_credentials=self.credentials)
        ### Opensearch aws
        
        ### bedrock embeddings
        self.embeddings = kwargs.get("embedding_object")
        ### bedrock embeddings
       
    def create_ensemble_retriever(self, retriever_list: List[Tuple], query: str, filters: Dict, frontend_filter_fields: Dict) -> EnsembleRetriever:
        """
        Creates an ensemble retriever.

        Args:
            retriever_list (List): A list of retriever definitions.
            query (str): The query string.
            filters (Dict): The filters for the query.
            frontend_filter_fields (Dict): The frontend filters name conversion dictionary.

        Returns:
            EnsembleRetriever: The ensemble retriever object.
        """
        retriever_list_output = []
        retriever_weights_output = []
        kw_structured_docs = {}
        
        match_text_query = {"match": {"text": query}}
        if len(filters) > 0:
            dct_filters_list = []
            for key, value_ in filters.items():
                if len(value_) == 1:
                    value = value_[0]
                    dct_filters_list.append({"term": {f"metadata.{frontend_filter_fields.get(key, key)}.keyword": value}})
                else:
                    should_conditions = []
                    nested_should_conditions = []
                    for value in value_:
                        nested_should_conditions.append({"term": {f"metadata.{frontend_filter_fields.get(key, key)}.keyword": value}})
                    should_conditions.append({"bool": {"should": nested_should_conditions}})
                    dct_filters_list.append({"bool": {"should": should_conditions}})


        for retriever_definition in retriever_list:
            if retriever_definition[0] == "bm_25" or retriever_definition[0] == "tf_idf":
                if retriever_definition[2] not in kw_structured_docs:
                    kw_client = OpenSearch(
                    hosts=self.opensearch_address,
                    http_auth=self.auth,
                    use_ssl=True,
                    verify_certs=True,
                    connection_class=RequestsHttpConnection,
                    timeout=30)
                    
                    # filtering on documents for kw search
                    if len(filters) > 0:
                        total_filter_query = [match_text_query] + dct_filters_list
                        body = {
                            "query": {
                                "bool": {
                                    "must": total_filter_query
                                }
                            }
                        }
                    else:
                        body={"query": {"match": {"text": query}}}

                    results = kw_client.search(index=retriever_definition[2],body=body)
                    structured_docs = []
                    for r in results["hits"]["hits"]:
                        structured_docs.append(Document(page_content=r["_source"]["text"], metadata=r["_source"]["metadata"]))
                    kw_structured_docs[retriever_definition[2]] = structured_docs

                else:
                    structured_docs = kw_structured_docs[retriever_definition[2]]
                                    
                # filtering on documents for kw search
                if len(structured_docs):
                    if retriever_definition[0] == "bm_25":
                        retriever = BM25Retriever.from_documents(structured_docs, k = self.k_documents)
                        retriever_list_output.append(retriever)
                        retriever_weights_output.append(retriever_definition[1])
                    elif retriever_definition[0] == "tf_idf":
                        retriever = TFIDFRetriever.from_documents(structured_docs, k = self.k_documents)
                        retriever_list_output.append(retriever)
                        retriever_weights_output.append(retriever_definition[1])
                    else:
                        # not implemented error
                        raise NotImplementedError()
                
            elif retriever_definition[0] == "embeddings":
                semantic_vectorstore = OpenSearchVectorSearch(
                    opensearch_url=self.opensearch_address,
                    http_auth=self.auth,
                    timeout=30,
                    use_ssl=True,
                    verify_certs=True,
                    connection_class=RequestsHttpConnection,
                    index_name=retriever_definition[2], 
                    embedding_function=self.embeddings
                )
                if len(filters) > 0:
                    body = {
                        "k": self.k_documents,
                        "filter": {
                            "bool": {
                                "must": dct_filters_list
                            }
                        }
                    }
                else:
                    body = {"k": self.k_documents}
                retriever = semantic_vectorstore.as_retriever(search_kwargs=body)
                retriever_list_output.append(retriever)
                retriever_weights_output.append(retriever_definition[1])

            else:
                # not implemented error
                raise NotImplementedError()
        ensemble_retriever = EnsembleRetriever(retrievers=retriever_list_output, weights=retriever_weights_output)
        return ensemble_retriever 
    
    def create_parent_retriever(self, ensemble_retriever: EnsembleRetriever, parent_collection_name: str):
        """
        Creates a parent retriever.

        Args:
            ensemble_retriever (EnsembleRetriever): The ensemble retriever object.
            parent_collection_name (str): The name of the parent collection.

        Returns:
            ParentRetriever: The parent retriever object.
        """
        parent_client = OpenSearch(
            hosts=self.opensearch_address,
            http_auth=self.auth,
            use_ssl=True,
            verify_certs=True,
            connection_class=RequestsHttpConnection,
            timeout=30,
        )
        parent_retreiver = ParentRetriever(ensemble_retriever = ensemble_retriever, client_parent=parent_client, parent_metadata_child = self.parent_metadata_child, parent_metadata_parent = self.parent_metadata_parent, index_name=parent_collection_name, child_parent_key_attribute= self.child_parent_key_attribute,parent_chunk_ordering=self.parent_chunk_ordering_metadata)
    
        return parent_retreiver
        
        
        
    
    def retrieve_documents_with_metadata(self, query:str, **metadata) -> List[Dict]:
        """
        Retrieves documents with metadata based on a query and optional filters.

        Args:
            query (str): The query string.
            metadata (Dict): Additional metadata for the query. Filters are expected to be in the "filters" key.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries representing retrieved documents with metadata.
        """
        
        filters = metadata.get("filters", {})
        ensemble_retriever = self.create_ensemble_retriever(self.retrievers_list, query, filters, self.frontend_filter_fields)
        parent_retreiver = self.create_parent_retriever(ensemble_retriever = ensemble_retriever, parent_collection_name=self.parent_collection_name,)
        retrieved_documents_ = parent_retreiver.get_relevant_documents(query)

        retrieved_documents = []
        for doc in retrieved_documents_:
            retrieved_documents__ = {}

            retrieved_documents__["text"] = doc.page_content
            for key, value in doc.metadata.items():
                retrieved_documents__[key] = value
            retrieved_documents.append(retrieved_documents__)

        return retrieved_documents
    
    def retrieve_documents(self, query:str, **metadata) -> List[str]:
        """
        Retrieves documents based on a query and optional filters.

        Args:
            query (str): The query string.
            metadata (Dict): Additional metadata for the query. Filters are expected to be in the "filters" key.

        Returns:
            List[str]: A list of retrieved documents.
        """
        full_retrieved_documents = self.retrieve_documents_with_metadata(query, **metadata)
        retrieved_documents = [doc["text"] for doc in full_retrieved_documents]
        return retrieved_documents
