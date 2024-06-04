import time

from genai_core.cores.LLMs.LLM_base import LLM


class MockLLM(LLM):
    
    def __init__(self, **kwargs):
        self.default_answer = "Hello I'm Giada! I can't do anything for you right now but soon I'll be able to answer your needs :)"
        
    def generate_answer(self, question: str) -> str:
        for i in range(0, len(self.default_answer), 3):
            yield self.default_answer[i:i+3]
            time.sleep(0.055)
            
            
    def generate_answer_batch(self, question: str, debug: bool = False, **kwargs)-> str:
        """
        Function to quickly generate an answer in batch using the Bedrock API
        Args:
            question: str
            debug: bool (default: False) --> if True, print the question
            kwargs: dict
                prompt_template: str (default: None)
                conversation_history: list (default: None) -> list of tuples (str, str), where the first element is the user / assistant and the second element is the message
                task: str (default: None)
                context: list (default: None) -> list of strings
        Returns:
            str
        """
        answer = ""

        for chunk in self.generate_answer(question, debug, **kwargs):
            answer+=chunk
        
        return answer
        
        