from genai_core.logger.logger import Logger

logger=Logger()

class Orchestrator:
    """
    An orchestrator class for managing completion progress and preparation tasks.

    Methods:
        is_completion(event: Any) -> bool: Checks completion progress based on the event.
        prepare(event: Any) -> None: Prepares the event for further processing.
    """

    def is_completion(self, event): 
        """
        Checks if the completion progress is reached based on the event's state.

        Args:
            event (Any): The event object containing the state information.

        Returns:
            bool: True if completion progress is reached, False otherwise.
        """
        state_ = event.kwargs.get("state")
        logger.info("checking completion progress")
        return set(state_["needed_info"]) == set(state_["current_info"])
        #return a==2
        
    def prepare(self, event):
        """
        Prepares the event for further processing.

        Args:
            event (Any): The event object to be prepared.
        """
        pass