from abc import ABC, abstractmethod
from typing import List
from genai_core.logic_blocks.base_block import Block

class BaseIntentClassificator(ABC):
    """
    An abstract base class for intent classification systems, defining a method to determine the intent
    of a given query.

    Attributes:
        None
    """
    @abstractmethod
    def get_intent(self, query: str, possible_intents:List[str]) -> List[str, Block]:
        """
        Determines the intent of a given query.

        Args:
            query (str): The query to classify.
            possible_intents (List[str]): A list of possible intents that could match the query.

        Returns:
            Union[str, Block]: Either the predicted intent or a Block corresponding to the predicted intent.
        """
        pass