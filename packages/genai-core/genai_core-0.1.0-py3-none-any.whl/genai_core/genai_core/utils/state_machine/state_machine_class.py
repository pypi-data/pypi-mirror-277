from genai_core.utils.state_machine.state import ChatBotState
from genai_core.utils.state_machine.orchestrator import Orchestrator
from transitions import Machine
from genai_core.logger.logger import Logger

logger=Logger()    

class StateMachine:
    """
    A class representing a state machine for managing transitions and states.

    Attributes:
        state_machine (Any): The state machine object.
        orchestrator (Any): The orchestrator object.
    """
    def __init__(self, state_machine: Machine, orchestrator: Orchestrator):
        """
        Initializes a StateMachine instance.

        Args:
            state_machine (Any): The state machine object.
            orchestrator (Any): The orchestrator object.
        """
        self.state_machine = state_machine
        self.orchestrator = orchestrator
        
    def get_state(self) -> ChatBotState:
        """
        Gets the current state of the state machine.

        Returns:
            ChatBotState: The current state of the state machine.
        """
        logger.info("get machine state")
        return self.state_machine.get_state(self.orchestrator.state)
    
    def set_state(self, state: str) -> bool:
        """
        Sets the state of the state machine.

        Args:
            state (Any): The state to set.

        Returns:
            bool: True if the state is successfully set, False otherwise.
        """
        return self.state_machine.set_state(state)
    
    def transition(self, intent: str, state: str) -> bool:
        """
        Performs the next transition based on the intent and state.

        Args:
            intent (Any): The intent for transition.
            state (Any): The state for transition.

        Returns:
            bool: True if the transition is successful, False otherwise.
        """
        logger.info("perform next transition")
        return self.orchestrator.trigger(intent, state=state)
