from openai import OpenAI
from openai.types.chat import ChatCompletion
from dotenv import load_dotenv

## set ENV variables
load_dotenv()
client = OpenAI()

def completion(messages, tools=None, model="gpt-4o-mini"):
    response: ChatCompletion = client.chat.completions.create(
        model=model,
        messages=messages,
        tools=tools,
    )
    return {
        "response": response,
        "message": response.choices[0].message
    }