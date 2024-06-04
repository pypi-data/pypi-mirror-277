import boto3
import json
import yaml
import json

from genai_core.core.LLMs.LLM_base import LLM
from botocore.config import Config
from anthropic_bedrock import AnthropicBedrock 
from genai_core.config.cfg import BEDROCK_MODEL_PARAMS
from typing import List, Tuple
from genai_core.logger.logger import Logger

logger=Logger()

class BedrockLLM(LLM):
    """
    This class is designed to interface with the Bedrock API to generate answers using large language models.
    It handles conversation history, context refactoring, and streaming/batch answer generation with customization options.

    Attributes:
        answer_id (str): the id of the current message 
        boto3_session (boto3.Session): A session for boto3 AWS SDK.
        region (str): The cloud region where the Bedrock API is hosted. 
        service (str): The Bedrock runtime service name.
        model_id (str): Identifier for the specific model to be used.
        temperature (float): Controls randomness in the answer generation.
        max_tokens_to_sample (int): The maximum number of tokens to generate.
        top_p (float): Nucleus sampling parameter controlling the size of the probability mass to sample from.
        top_k (int): Controls diversity for the generated answer.
        proxy_definitions (Dict): Proxies configuration for the HTTP client.
        model_tokens (Dict[str, int]): Mapping of model IDs to their token limits.
        client (boto3.client): The boto3 client configured for interacting with the Bedrock API.
        billing_name (str): name of the part that generates costs
    """
    
    
    def __init__(self, answer_id:str,  **kwargs):
        """
        Args:
            region: str (default: "eu-central1")
            service: str (default: "bedrock-runtime")
            model_id: str (default: "anthropic.claude-v2")
            temperature: float (default: 0.5)
            max_tokens_to_sample: int (default: 500)
            top_p: float (default: 1)
            top_k: int (default: 250)
            proxy_definitions: dict (default: {})
            model_tokens: dict (default: {}) --> {model_id: int}
            billing_name (str): name of the part that generates costs
        """
        super().__init__(answer_id)
        self.boto3_session = boto3.Session(
            region_name='eu-central-1',
            aws_access_key_id="AKIAZF6FN5AJ3D5TNTM7",
            aws_secret_access_key="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",
        )
        self.billing_name = kwargs.get("billing_name", "default_LLM_generation") 
        self.region = kwargs.get("region") if "region" in kwargs else "eu-central1"
        self.service = kwargs.get("service") if "service" in kwargs else "bedrock-runtime"
        self.model_id = kwargs.get("model_id") if "model_id" in kwargs else "anthropic.claude-v2"
        self.temperature = kwargs.get("temperature") if "temperature" in kwargs else 0.5
        self.max_tokens_to_sample = kwargs.get("max_tokens_to_sample") if "max_tokens_to_sample" in kwargs else 500
        self.top_p = kwargs.get("top_p") if "top_p" in kwargs else 1
        self.top_k = kwargs.get("top_k") if "top_k" in kwargs else 250

        self.proxy_definitions = kwargs.get("proxy_definitions") if "proxy_definitions" in kwargs else {}
        self.model_tokens =  BEDROCK_MODEL_PARAMS["model_tokens"]
        self.client = self.boto3_session.client(self.service, config = Config(proxies=self.proxy_definitions))
        self.last_interaction_input_tokens =  0 
        self.last_interaction_output_tokens =  0

    def refactor_conversation_history(self, conversation_history: List[Tuple])-> str:
        """
        Refactors a conversation history into a string format suitable for model input.

        Args:
            conversation_history: A list of tuples where each tuple represents a dialog turn
                                  with the first element being the speaker and the second element the spoken text.

        Returns:
            A single string representing the refactored conversation history.
        """
        string = ""
        for i in conversation_history:
            if i[0] == "user":
                agent = "H"
            elif i[0] =="system":
                agent = "A"
            else:
                agent= "S"
            string += agent + ":" + i[1] + " \n"
        return string
    
    def refactor_context(self, prompt_template: str,context: List[str], **kwargs)-> str:
        """
        Refactors the context by considering token limits of the model and constructs a context string.

        Args:
            prompt_template: The template string used for generating prompts.
            kwargs: Additional dict for prompt customization.
                prompt_template: str (default: None)
                conversation_history: list (default: None) -> list of tuples (str, str), where the first element is the user / assistant and the second element is the message
                task: str (default: None)
                context: list (default: None) -> list of strings
            context: A list of context strings to be considered for inclusion.

        Returns:
            A string representation of the context, considering model token limits.
        """
        
        if self.model_id in self.model_tokens:
            max_model_tokens = self.model_tokens[self.model_id]
            client_ab = AnthropicBedrock()
            prompt_template_nocontext = prompt_template.replace("{context}", "")
            prompt_nocontext = prompt_template_nocontext.format(**kwargs)
            prompt_nocontext_tokens = client_ab.count_tokens(prompt_nocontext)
            total_nocontext_tokens = prompt_nocontext_tokens + self.max_tokens_to_sample

            if total_nocontext_tokens < max_model_tokens:
                context_string = "\n"
                for ctx in context:
                    if client_ab.count_tokens(ctx) + total_nocontext_tokens < max_model_tokens:
                        context_string += ctx + " \n"
                        total_nocontext_tokens += client_ab.count_tokens(ctx)
                return context_string
            else:
                return ""

        else:
            return ""
        
    def streaming_generate_answer_(self, question: str, **kwargs)-> str:
        """
        Streams the response from the Bedrock API as a generator of text chunks.

        Args:
            question: The question or prompt to generate an answer for.

        Yields:
            Chunks of text as part of the answer from the model.
        """
        model_kwargs = {
            "temperature": self.temperature,
            "max_tokens_to_sample": self.max_tokens_to_sample,
            "top_p": self.top_p,
            "top_k": self.top_k,
            "prompt": question
        }
        response_stream = self.client.invoke_model_with_response_stream(
            body=json.dumps(model_kwargs),
            modelId=self.model_id,
            accept='application/json',
            contentType='application/json'
        )
        if response_stream:
            status_code = response_stream['ResponseMetadata']['HTTPStatusCode']
            if status_code != 200:
                raise ValueError(f"Error invoking Bedrock API: {status_code}")
            for response in response_stream['body']:
                json_response = json.loads(response['chunk']['bytes'])
                #print(json_response['completion'], flush = True, end = "")
                yield json_response['completion']
    
    def _fill_prompt(self, question: str, **kwargs) -> str:
        """
        Fills in the provided prompt template with the question and additional context or arguments.

        Args:
            question: The input question or prompt text.
            kwargs: Additional dict for prompt customization.
                prompt_template: str (default: None)
                conversation_history: list (default: None) -> list of tuples (str, str), where the first element is the user / assistant and the second element is the message
                task: str (default: None)
                context: list (default: None) -> list of strings

        Returns:
            A string with the filled prompt ready for model generation.
        """
        template_args = {}
        prompt_template = kwargs.get("prompt_template")
        template_args["question"] = question 
        forbidden_keys = ["question", "prompt_template", "model_tokens", "context"]

        if "conversation_history" in kwargs:
            kwargs["conversation_history"] = self.refactor_conversation_history(kwargs["conversation_history"])

        for key, value in kwargs.items():
            if key not in forbidden_keys:
                template_args[key] = value
        if "context" in kwargs:
            template_args["context"] = self.refactor_context(prompt_template, kwargs["context"], **template_args)
        new_question = prompt_template.format(**template_args)
        return new_question
    
    def _get_tokens(self, text: str) -> int:
        client_ab = AnthropicBedrock()
        return client_ab.count_tokens(text)      
         
    def generate_answer(self, question: str, debug: bool = False, **kwargs)-> str:
        """
        Generates an answer for the given question, streaming the response.

        Args:
            question: The question to generate an answer for.
            debug: If True, prints additional debug information.
            kwargs: Additional dict for prompt customization.
                prompt_template: str (default: None)
                conversation_history: list (default: None) -> list of tuples (str, str), where the first element is the user / assistant and the second element is the message
                task: str (default: None)
                context: list (default: None) -> list of strings

        Yields:
            Chunks of the generated answer as they are received.
        """


        question = question.strip()
        if not question.startswith("Human:") and "prompt_template" not in kwargs:
            question = "Human: " + question
        if not question.endswith("Human:") and "prompt_template" not in kwargs:
            question = question + " Assistant: "   

        if "prompt_template" in kwargs:
            question = self._fill_prompt(question,**kwargs)
        
        input_tokens = self._get_tokens(question)
        string = ""
        for chunk in self.streaming_generate_answer_(question):
            string += chunk
            yield chunk
        output_tokens = self._get_tokens(string)
        self._save_tokens(input_tokens, output_tokens)

    def generate_answer_batch(self, question: str, debug: bool = False, **kwargs)-> str:
        """
        Generates an answer in a batch mode by concatenating chunks received from the streaming generator.

        Args:
            question: The question to generate an answer for.
            debug: If True, prints additional debug information.
            kwargs: Additional dict for prompt customization.
                prompt_template: str (default: None)
                conversation_history: list (default: None) -> list of tuples (str, str), where the first element is the user / assistant and the second element is the message
                task: str (default: None)
                context: list (default: None) -> list of strings

        Returns:
            A complete answer as a single string.
        """
        answer = ""

        for chunk in self.generate_answer(question, debug, **kwargs):
            answer+=chunk
        
        return answer
    
    def _save_tokens(self, input_tokens: int , output_tokens: int):
        tokens = {"model_id": self.model_id, "model_type": "bedrock-api",  "input_tokens": input_tokens, "output_tokens": output_tokens}
        try:
            with open(self.answer_id+".json","r") as f:
                tokens_dict = json.load(f)   
            if self.billing_name in tokens_dict:
                tokens_dict[self.billing_name]["input_tokens"]  += input_tokens   
                tokens_dict[self.billing_name]["output_tokens"]  += output_tokens     
            else:   
                tokens_dict[self.billing_name] = tokens   
        except FileNotFoundError as e:
            tokens_dict = {}
            tokens_dict[self.billing_name] = tokens          
           
        
        with open(self.answer_id+ ".json","w") as f:
            json.dump(tokens_dict,f)
        logger.info(f"Tokens count for {self.billing_name}: {tokens}", cost_center = self.billing_name)