from abc import ABC, abstractmethod

class LLM(ABC):
    """
    An abstract base class for language generation models (LLMs), defining methods to generate answers
    either for single questions or in batch mode.

    Attributes:
        answer_id: the id of the current message
    """
    def __init__(self, answer_id: str):
        self.answer_id = answer_id

    
    @abstractmethod
    def generate_answer(self, question: str, debug: bool = False, **kwargs)-> str:
        """
        Generates an answer for a single question using the LLM.

        Args:
            question (str): The question for which to generate an answer.
            debug (bool, optional): A flag indicating whether to include debug information. Defaults to False.
            **kwargs: Additional keyword arguments specific to the implementation.

        Returns:
            str: The generated answer.
        """
        pass
    
    @abstractmethod
    def generate_answer_batch(self, question: str, debug: bool = False, **kwargs)-> str:
        """
        Generates answers for a batch of questions using the LLM.

        Args:
            questions (List[str]): The list of questions for which to generate answers.
            debug (bool, optional): A flag indicating whether to include debug information. Defaults to False.
            **kwargs: Additional keyword arguments specific to the implementation.

        Returns:
            str: The generated answers.
        """
        pass
    
