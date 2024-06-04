import re

from genai_core.functions.question_rephrasing.base_question_rephrasing import BaseQuestionRephrasing
from genai_core.cores.LLMs.LLM_base import LLM
from typing import List, Tuple

class QuestionRephrasing(BaseQuestionRephrasing):
    """
    A class implementing question rephrasing functionality using a large language model (LLM).

    Attributes:
        prompt (str): The prompt template used for generating rephrased questions.
        llm (LLM): An instance of a large language model used for generating responses.
        chat_history_length_limit (int): The maximum length limit of chat history considered for rephrasing.
    """
    
    def __init__(self, prompt: str, llm_block: LLM, **kwargs):
        """
        Initializes the QuestionRephrasing with a prompt template and a large language model.

        Args:
            prompt (str): The prompt template used for generating rephrased questions.
            llm_block (LLM): An instance of a large language model used for generating responses.
            **kwargs: Additional keyword arguments including:
                      - chat_history_length_limit (int, optional): The maximum length limit of chat history
                        considered for rephrasing (default is 10).
        """
        self.prompt = prompt
        self.llm = llm_block
        self.chat_history_length_limit = kwargs.get("chat_history_length_limit",10)
        
    def rephrase_question(self, question: str, chat_history: List[Tuple]) -> str:
        """
        Rephrases the given question using a large language model based on the provided chat history.

        Args:
            question (str): The original question to be rephrased.
            chat_history (List[Tuple]): The history of the chat, used for context in rephrasing.

        Returns:
            str: The rephrased question.
        """
        if not(chat_history):
            rephrased_question=question
        else:
            new_q=self.llm.generate_answer_batch(question,prompt_template=self.prompt, chat_history=chat_history[-(self.chat_history_length_limit*2):])
            follow_up_pattern = re.compile(r"<FOLLOW-UP>(.*?)<\/FOLLOW-UP>", re.DOTALL)
            new_tag_pattern = re.compile(r"<NEW>(.*?)<\/NEW>", re.DOTALL)

            # Search for matches.
            follow_up_match = follow_up_pattern.search(new_q)
            new_tag_match = new_tag_pattern.search(new_q)

            # Determine the output based on the match found.
            if follow_up_match:
                rephrased_question = follow_up_match.group(1).strip()
            elif new_tag_match:
                rephrased_question = question
            else:
                rephrased_question = question
        return rephrased_question
    
