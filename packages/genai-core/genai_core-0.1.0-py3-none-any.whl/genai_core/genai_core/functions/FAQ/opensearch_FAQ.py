import boto3

from langchain_community.vectorstores import OpenSearchVectorSearch
from opensearchpy import OpenSearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
from genai_core.functions.FAQ.base_FAQ import BaseFAQ
from genai_core.cores.embedding_models.base_model import BaseEmbeddingModel
from typing import Union, List, Dict
from genai_core.logger.logger import Logger

logger=Logger()

class OpensearchFAQ(BaseFAQ):
    """
    A class for interfacing with an OpenSearch database to provide answers to frequently asked questions
    using a specified embedding model for semantic search.

    Attributes:
        threshold (float): The similarity threshold for considering an answer relevant.
        connection_string (str): The URL for the OpenSearch database connection.
        collection_name (str): The name of the collection within the OpenSearch database to query against.
        embeddings (BaseEmbeddingModel): The embedding model used for generating question embeddings.
        os_client (OpenSearch): The OpenSearch client for database operations.
        vectorstore (OpenSearchVectorSearch): A specialized vector search client for embedding-based searches.
    """
    
    def __init__(self, embedding_object: BaseEmbeddingModel, **kwargs):
        """
        Initializes the OpensearchFAQ object with a given embedding model and optional configuration parameters.

        Args:
            embedding_model (BaseEmbeddingModel): The embedding model to use for question similarity comparison.
            **kwargs: Arbitrary keyword arguments. Currently supports 'threshold', 'connection_string', and 'collection_name'.
        """
        ## config params
        self.threshold = kwargs.get("threshold") if "threshold" in kwargs else 0.99
        self.connection_string = kwargs.get("connection_string")
        self.collection_name = kwargs.get("collection_name") if "collection_name" in kwargs else "faq_index_audit"     
        

        self.embeddings = embedding_object 
        
        credentials = boto3.Session(region_name="eu-central-1").get_credentials()
        auth = AWS4Auth(region="eu-central-1", service='es', refreshable_credentials=credentials)

        self.os_client = OpenSearch(
            hosts=self.connection_string,
            http_auth=auth,
            use_ssl=True,
            verify_certs=True,
            connection_class=RequestsHttpConnection,
            timeout=30,
        )
    
        self.vectorstore = OpenSearchVectorSearch(
            opensearch_url=self.connection_string,
            http_auth=auth,
            timeout=30,
            use_ssl=True,
            verify_certs=True,
            connection_class=RequestsHttpConnection,
            index_name= self.collection_name,
            embedding_function=self.embeddings
        )

    def get_faq_answer(self, question: str, **kwargs) -> [Union[str, None], Union[str, None], List[Dict]]:
        """
        Retrieves the most relevant FAQ answer for a given question from the OpenSearch database,
        if the similarity score exceeds the defined threshold. Updates the 'frequency' metadata for
        the FAQ entry upon a successful match.

        Parameters:
            question (str): The question for which an FAQ answer is sought.
            **kwargs: Arbitrary keyword arguments. Not used in this method but included for extensibility.

        Returns:
            Union[str, None]: The answer to the given question if a relevant match is found and exceeds
            the similarity threshold; otherwise, None.
        """
        #check sulla similarity
        sources = []
        if self.vectorstore.similarity_search_with_score(question.lower(),search_type="painless_scripting", space_type="cosineSimilarity",k=1,)[0][1]-1 > self.threshold:
            document = self.vectorstore.similarity_search_with_score(question.lower(),search_type="painless_scripting", space_type="cosineSimilarity",k=1,)[0][0]
            answer=document.metadata['answer']
            ###ricerco l'id della domanda in opensearch
            question=document.page_content
            sources = document.metadata["sources_info"]
            logger.info(f"FAQ found! Question:{question}")
            search_query = {
            'query': {
                'match': {
                    'text': question
                    }
                }
            }
            # Eseguo la ricerca ed estraggo l'indice
            response = self.os_client.search(
                index=self.collection_name,
                body=search_query
            )
            doc_id=response['hits']['hits'][0]['_id']
            field_to_update = 'frequency'

            #UPDATE DELLA FREQUENCY
            new_value = self.vectorstore.similarity_search_with_score(question.lower(),search_type="painless_scripting", space_type="cosineSimilarity",k=1,)[0][0].metadata['frequency'] +1
            script = {
            'script': {
                'source': 'ctx._source.metadata.frequency = params.new_value',
                'lang': 'painless',
                'params': {
                    'new_value': new_value
                    }
                }
            }
            response = self.os_client.update(
                index=self.collection_name,
                id=doc_id,
                body=script
            )
        else:
            answer=None
            question=None
        
        return answer, question, sources

        
        
        