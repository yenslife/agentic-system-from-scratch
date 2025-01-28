from openai import OpenAI
from dotenv import load_dotenv

## set ENV variables
load_dotenv()
client = OpenAI()

def inference(messages, tools=None, model="gpt-4o-mini"):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        tools=tools,
    )
    return {
        "response": response,
    }