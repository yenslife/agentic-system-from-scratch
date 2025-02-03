from typing import Callable
from .type import CompletionResponse

class ProviderRegistry:
    _providers: dict[str, Callable] = {}

    @classmethod
    def register(cls, name: str, completion_func: Callable):
        """註冊一個 provider 的 completion function"""
        cls._providers[name] = completion_func

    @classmethod
    def get(cls, name: str) -> Callable:
        """取得指定的 completion function"""
        if name not in cls._providers:
            raise ValueError(f"Provider '{name}' not found. Available providers: {list(cls._providers.keys())}")
        return cls._providers[name]

# Import and register providers
from .openai import completion as openai_completion
from .ollama import completion as ollama_completion

ProviderRegistry.register("openai", openai_completion)
ProviderRegistry.register("ollama", ollama_completion)

def get_completion(provider: str) -> Callable[..., CompletionResponse]:
    """Get completion function for specified provider"""
    return ProviderRegistry.get(provider)