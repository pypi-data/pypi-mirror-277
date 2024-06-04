from transitions import State
from typing import List
from genai_core.logger.logger import Logger

logger=Logger()

class ChatBotState(State):
    """
    A class representing a state of the chatbot.

    Attributes:
        name (str): The name of the state.
        prompt (str): The prompt associated with the state.
        intents (List[str]): A list of intents associated with the state.
    """
    def __init__(self, name: str, prompt: str, intents: List[str]):
        """
        Initializes a ChatBotState instance.

        Args:
            name (str): The name of the state.
            prompt (str): The prompt associated with the state.
            intents (List[str]): A list of intents associated with the state.
        """
        super().__init__(name)
        self.prompt = prompt
        self.intents = intents