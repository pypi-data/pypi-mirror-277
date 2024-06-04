from abc import ABC, abstractmethod
from typing import List


class BasePromptRouting(ABC):
    """
    An abstract base class defining the interface for prompt routing functionality.

    Methods:
        get_prompt: Abstract method to be implemented by subclasses for generating prompts based on questions.
    """
    
    @abstractmethod
    def get_prompt(self, question: str, **kwargs) -> List[str, str]:
        """
        Abstract method to generate prompts based on the provided question.

        Args:
            question (str): The question for which a prompt is to be generated.
            **kwargs: Additional keyword arguments that might be used by specific implementations.

        Returns:
            str: The generated prompt.
        """
