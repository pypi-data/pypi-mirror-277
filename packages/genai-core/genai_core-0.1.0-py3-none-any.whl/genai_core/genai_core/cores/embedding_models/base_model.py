from abc import ABC, abstractmethod
from typing import List

class BaseEmbeddingModel(ABC):
    """
    An abstract base class for embedding models, defining methods to embed queries and documents.

    Attributes:
        answer_id (str): the id of the current message 
    """
    
    def __init__(self, answer_id:str):
        self.answer_id=answer_id
        
    @abstractmethod
    def embed_query(self, text: str) -> List[float]:
        """
        Embeds a single query text.

        Args:
            text (str): The text to embed.

        Returns:
            List[float]: The embedding for the text.
        """
        pass
    
    @abstractmethod        
    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """
        Embeds a list of document texts.

        Args:
            texts (List[str]): The list of texts to embed.

        Returns:
            List[List[float]]: The list of embeddings, one for each text.
        """
        pass
    
    
    
    