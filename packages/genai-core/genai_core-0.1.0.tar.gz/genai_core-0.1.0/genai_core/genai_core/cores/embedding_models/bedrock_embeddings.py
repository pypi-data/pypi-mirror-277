import json
import boto3
import asyncio
import numpy as np

from genai_core.cores.embedding_models.base_model import BaseEmbeddingModel
from botocore.config import Config
from typing import List
from langchain_core.runnables.config import run_in_executor
from genai_core.logger.logger import Logger

logger=Logger()


class BedrockEmbeddingModel(BaseEmbeddingModel):
    
    def __init__(self,answer_id: str, **kwargs):
        """
        Initializes the BedrockEmbeddingModel.

        Args:
            answer_id (str): the id of the current message 
            model_id (str, optional): The ID of the model used for embedding generation. Defaults to "amazon.titan-embed-text-v1".
            proxy_definitions (dict, optional): A dictionary containing proxy definitions. Defaults to {}.
            normalize (bool, optional): A flag indicating whether to normalize the embeddings. Defaults to False.
            billing_name (str): name of the part that generates costs

        """
        super().__init__(answer_id)
        self.billing_name = kwargs.get("billing_name", "default_text_embedding") 
        self.model_id = kwargs.get("model_id") if "model_id" in kwargs else "amazon.titan-embed-text-v1"
        self.proxy_definitions = kwargs.get("proxy_definitions") if "proxy_definitions" in kwargs else {}
        self.client = boto3.Session(
            region_name='eu-central-1',
            aws_access_key_id="AKIAZF6FN5AJ3D5TNTM7",
            aws_secret_access_key="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",
        ).client("bedrock-runtime", config = Config(proxies=self.proxy_definitions))
        self.normalize =  kwargs.get("normalize") if "normalize" in kwargs else False
        
        
    def _normalize_vector(self, embeddings: List[float]) -> List[float]:
        """
        Normalize the embedding to a unit vector.

        Args:
            embeddings (List[float]): The embedding to normalize.

        Returns:
            List[float]: The normalized embedding.
        """
        emb = np.array(embeddings)
        norm_emb = emb / np.linalg.norm(emb)
        return norm_emb.tolist()

    def _embedding_func(self, text: str, **kwargs)-> List[float]:
        """
        Generate embeddings for the given text.

        Args:
            text (str): The text for which to generate embeddings.

        Returns:
            List[float]: The generated embeddings.
        """
        response = self.client.invoke_model(
            body=json.dumps({"inputText": text}),
            modelId=self.model_id,
            accept='application/json',
            contentType='application/json'
        )
        response_body = json.loads(response['body'].read())
        if "cohere" in self.model_id:
            self._save_tokens(response_body["meta"]["billed_units"]["input_tokens"])
            return response_body.get("embeddings")[0]
        else:
            self._save_tokens(response_body['inputTextTokenCount'])
            return response_body.get('embedding')
        
        
    def embed_query(self, text: str) -> List[float]:
        """
        Compute query embeddings using a Bedrock model.

        Args:
            text (str): The text to embed.

        Returns:
            List[float]: Embeddings for the text.
        """
        embedding = self._embedding_func(text)

        if self.normalize:
            return self._normalize_vector(embedding)

        return embedding
    
    
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
            """
            Compute document embeddings using a Bedrock model.

            Args:
                texts (List[str]): The list of texts to embed.

            Returns:
                List[List[float]]: List of embeddings, one for each text.
            """
            results = []
            for text in texts:
                response = self._embedding_func(text)

                if self.normalize:
                    response = self._normalize_vector(response)

                results.append(response)

            return results
        
    async def aembed_query(self, text: str) -> List[float]:
        """
        Asynchronously compute query embeddings using a Bedrock model.

        Args:
            text (str): The text to embed.

        Returns:
            List[float]: Embeddings for the text.
        """

        return await run_in_executor(None, self.embed_query, text)
    
    async def aembed_documents(self, texts: List[str]) -> List[List[float]]:
        """
        Asynchronously compute document embeddings using a Bedrock model.

        Args:
            texts (List[str]): The list of texts to embed.

        Returns:
            List[List[float]]: List of embeddings, one for each text.
        """

        result = await asyncio.gather(*[self.aembed_query(text) for text in texts])

        return list(result)

    def _save_tokens(self, text_tokens: int):
        tokens = {"model_id": self.model_id, "model_type": "bedrock-api",  "tokens": text_tokens}
        
        try:
            with open(self.answer_id+".json","r") as f:
                tokens_dict = json.load(f)   
            if self.billing_name in tokens_dict:
                tokens_dict[self.billing_name]["tokens"]  += text_tokens   
            else:   
                tokens_dict[self.billing_name] = tokens   
        except FileNotFoundError as e:
            tokens_dict = {}
            tokens_dict[self.billing_name] = tokens           
        
        with open(self.answer_id+".json","w") as f:
            json.dump(tokens_dict,f)
        logger.info(f"Tokens count for {self.billing_name}: {tokens}", cost_center=self.billing_name)
    
    
    