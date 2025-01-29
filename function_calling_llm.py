from rich import print

from model_providers.openai import completion
from prompts.fruit import (
    hello_message,
    tool_message,
    multiple_tool_message,
)
from tools.fruit import FRUIT_FUNCTION_SCHEMA as schema

# 定義兩個工具
tools = [schema["get_remain_fruit"], schema["get_fruit_info"]]

response = completion(hello_message, tools)["message"]
response_with_tool = completion(tool_message, tools)["message"]
response_with_multiple_tools = completion(multiple_tool_message, tools)["message"]

print("單純聊天的回覆",response)
print("偵測到需要工具的回覆", response_with_tool)
print("偵測到需要多個工具的回覆", response_with_multiple_tools)