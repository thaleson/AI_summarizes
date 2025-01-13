from abc import ABC, abstractmethod

class LLMInterface(ABC):
    @abstractmethod
    def chat_completion(self, messages: list, max_tokens: int, temperature: float, top_p: float) -> str:
        """Executa uma consulta no modelo LLM."""
        pass
