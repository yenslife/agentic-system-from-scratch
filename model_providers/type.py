from openai.types.chat import ChatCompletion, ChatCompletionMessage
from pydantic import BaseModel

class CompletionResponse(BaseModel):
    response: ChatCompletion
    message: ChatCompletionMessage