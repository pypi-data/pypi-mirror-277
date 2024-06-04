import joblib
import numpy as np
import boto3 

from genai_core.functions.intent_classification.base_classificator import BaseIntentClassificator
from genai_core.functions.question_rephrasing.base_question_rephrasing import BaseQuestionRephrasing
from genai_core.cores.embedding_models.base_model import BaseEmbeddingModel
from genai_core.logic_blocks.base_block import Block
from io import BytesIO
from typing import Dict, List, Tuple
from genai_core.logger.logger import Logger

logger=Logger()

class LGBMIntentClassificator(BaseIntentClassificator):
    """
    A class for intent classification using LightGBM models, capable of handling questions by classifying
    them into specific intents based on the embeddings generated from the questions to fit a pre-trained
    LightGBM models stored in an AWS S3 bucket.

    Attributes:
        models (Dict): A dictionary storing the LightGBM models loaded from S3, keyed by intent sets.
        class_mapping (Dict): A mapping from model prediction labels to intent labels.
        question_rephrasing (BaseQuestionRephrasing): An object used to rephrase questions for better classification.
        embedding_object (BaseEmbeddingModel): An object to generate embeddings from questions.
        blocks_dict (Dict[str, Block]): A mapping from intent labels to Block objects, which define the response actions.
    """
    
    def __init__(self,
                 bucket_name:str, 
                 model_mappings: Dict, 
                 class_mapping: Dict,
                 question_rephrasing_object:BaseQuestionRephrasing,
                 embedding_object: BaseEmbeddingModel,
                 blocks_dict: Dict[str, Block],
                 **kwargs):  
        """
        Initializes the LGBMIntentClassificator with model mappings, class mappings, a question rephrasing
        object, an embedding object, and a dictionary of blocks for response actions.

        Args:
            bucket_name (str): The name of the AWS S3 bucket containing the LightGBM models.
            model_mappings (Dict): A dictionary mapping intent sets to their corresponding model paths in S3.
            class_mapping (Dict): A dictionary mapping model output labels to intent labels.
            question_rephrasing_object (BaseQuestionRephrasing): An object for rephrasing questions.
            embedding_object (BaseEmbeddingModel): An object for generating embeddings from questions.
            blocks_dict (Dict[str, Block]): A dictionary mapping intent labels to response action blocks.
        """
        
        self.models = {}
        
        s3 = boto3.client('s3')
        for elem in model_mappings:
            response = s3.get_object(Bucket=bucket_name, Key=elem["model_path"])
            pickle_bytes = response['Body'].read()
            model = joblib.load(BytesIO(pickle_bytes))
            self.models[tuple(set(sorted(elem["intents"])))] = model
            
        self.class_mapping = class_mapping
        self.question_rephrasing = question_rephrasing_object 
        self.embedding_object = embedding_object
        self.blocks_dict = blocks_dict
            
    def get_intent(self, question: str, possible_intents:List[str], chat_history: List[Tuple], filters: Dict) -> List[str, Block]:
        """
        Determines the intent of a given question and returns the corresponding response block.

        If certain filters are set (e.g., "Generalist"), a predefined block is returned. Otherwise,
        the method predicts the intent based on the question's embedding and the provided possible intents,
        then returns the block associated with the predicted intent.

        Args:
            question (str): The question to classify.
            possible_intents (List[str]): A list of possible intents that could match the question.
            chat_history (List[Tuple]): The chat history, used for rephrasing the question if necessary.
            filters (Dict): A dictionary of filters that might affect the intent determination process.

        Returns:
            Union[Tuple[str, Block], Block]: Either a tuple containing the rephrased question and its corresponding
            Block, or a single Block if specific filters are met.
        """
        
        if "division" in filters and "Generalist" in filters["division"]:
            return question,self.blocks_dict["open_conversation"]
        
        if self.question_rephrasing:
            question = self.question_rephrasing.rephrase_question(question,chat_history)
            logger.info(f"Question rephrasing...OK. \nQuestion:{question},\nChat history:{chat_history}")
        embedding= self.embedding_object.embed_query(question)
        predicted_intent=np.argmax(self.models[tuple(set(sorted(possible_intents)))].predict(np.array([embedding])))
        class_label = self.class_mapping[predicted_intent]
        return question, self.blocks_dict[class_label]
            
        