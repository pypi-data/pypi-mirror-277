from abc import ABC, abstractmethod
from typing import List, Tuple

class BaseQuestionRephrasing(ABC):
    """
    An abstract base class defining the interface for question rephrasing functionality.

    Methods:
        rephrase_question: Abstract method to be implemented by subclasses for rephrasing questions.
    """
    
    @abstractmethod    
    def rephrase_question(question: str, chat_history:List[Tuple]) -> str:
        """
        Abstract method to rephrase a given question based on chat history.

        Args:
            question (str): The original question to be rephrased.
            chat_history (List[Tuple]): The history of the chat, used for context in rephrasing.

        Returns:
            str: The rephrased question.
        """
        pass