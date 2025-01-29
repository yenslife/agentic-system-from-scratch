import json
from rich import print

from model_providers.openai import completion, CompletionResponse
from prompts.fruit import (
    hello_message,
    tool_message,
    multiple_tool_message,
)
from tools.fruit import (
    FRUIT_FUNCTION_SCHEMA as schema,
    AVAILABLE_FUNCTIONS as functions
)

def run(messages: str, tools: list, model: str = "gpt-4o-mini") -> CompletionResponse:
    response = completion(messages, tools, model)

    if not response.message.tool_calls:
        return response

    print(f"Use Tool!!")
    messages.append(response.message) # must append model function call message
    for tool in response.message.tool_calls:
        function_name = tool.function.name
        function_args = json.loads(tool.function.arguments)
        function_to_call = functions[function_name]
        function_response = function_to_call(**function_args)
        print(f"Function: {function_name}, Args: {function_args}, Response: {function_response}")

        messages.append({
            "role": "tool",
            "tool_call_id": tool.id,
            "content": str(function_response)
        })

    return run(messages, tools, model) # 反覆迭代

if __name__ == "__main__":
    tools = [schema["get_remain_fruit"], schema["get_fruit_info"]]

    response = run(hello_message, tools)
    print("單純聊天的回覆",response.message)
    response_with_tool = run(tool_message, tools)
    print("偵測到需要工具的回覆", response_with_tool.message)
    response_with_multiple_tools = run(multiple_tool_message, tools)
    print("偵測到需要多個工具的回覆 (一次執行所有函式)", response_with_multiple_tools.message)