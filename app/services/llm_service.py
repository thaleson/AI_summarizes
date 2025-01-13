import os
from huggingface_hub import InferenceClient # type: ignore
from app.interfaces.llm_interface import LLMInterface # type: ignore

class LLMService(LLMInterface):
    def __init__(self, api_key: str, model_url: str):
        self.client = InferenceClient(api_key=api_key)
        self.model_url = model_url

    def chat_completion(self, messages: list, max_tokens: int, temperature: float, top_p: float) -> str:
        response = self.client.chat.completions.create(
            model=self.model_url,
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p
        )
        return response.choices[0].message['content']
