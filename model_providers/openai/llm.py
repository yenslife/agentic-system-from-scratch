from dataclasses import dataclass
from openai import OpenAI
from openai.types.chat import ChatCompletion, ChatCompletionMessage
from dotenv import load_dotenv

## set ENV variables
load_dotenv()
client = OpenAI()

@dataclass
class CompletionResponse():
    response: ChatCompletion
    message: ChatCompletionMessage

def completion(messages, tools=None, model="gpt-4o-mini") -> CompletionResponse:
    """因為我覺得要一直用 choices[0] 很煩所以抽象了這一層"""
    response: ChatCompletion = client.chat.completions.create(
        model=model,
        messages=messages,
        tools=tools,
    )
    return CompletionResponse(
        response=response,
        message=response.choices[0].message
    )