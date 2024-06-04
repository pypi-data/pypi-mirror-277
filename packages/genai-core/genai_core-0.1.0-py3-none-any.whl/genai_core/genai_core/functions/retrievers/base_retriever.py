from abc import ABC, abstractmethod
from typing import List, Dict

class Retriever(ABC):
    """
    An abstract base class for retrievers.

    Attributes:
        query (str): The query string.
        metadata (Dict): Additional metadata for the query.
    """
    
    @abstractmethod
    def retrieve_documents_with_metadata(query:str, **metadata) -> List[Dict]:
        """
        Retrieves documents with metadata based on a query and optional filters.

        Args:
            query (str): The query string.
            metadata (Dict): Additional metadata for the query.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries representing retrieved documents with metadata.
        """
        pass
    
    @abstractmethod        
    def retrieve_documents(query:str, **metadata) -> List[str]:
        """
        Retrieves documents based on a query and optional filters.

        Args:
            query (str): The query string.
            metadata (Dict): Additional metadata for the query.

        Returns:
            List[str]: A list of retrieved documents.
        """
        pass
        