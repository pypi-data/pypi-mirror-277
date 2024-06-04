from genai_core.logic_blocks.base_block import Block
from genai_core.functions.intent_classification.base_classificator import BaseIntentClassificator
from typing import Dict, List, Tuple

class MockIntentClassificator(BaseIntentClassificator):
    
    def __init__(self, blocks_dict:str, **kwargs):  
        self.blocks_dict = blocks_dict
        
    def get_intent(self, question: str, possible_intents:List[str], chat_history: List[Tuple], filters: Dict) -> List[str, Block]:  
        return question,self.blocks_dict["rag"]
            
        