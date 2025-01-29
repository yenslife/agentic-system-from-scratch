from rich import print

from model_providers.openai import inference
from prompts.fruit import (
    hello_message,
    tool_message,
    multiple_tool_message,
)

# 定義兩個工具
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_remain_fruit",
            "description": "取得指定水果的剩餘數量",
            "parameters": {
                "type": "object",
                "properties": {
                    "fruit_name": {
                        "type": "string",
                        "description": "指定水果名稱，可以是繁體中文或者是英文 e.g. 香蕉、banana",
                    }
                },
                "required": ["fruit_name"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_fruit_info",
            "description": "取得指定水果的詳細資訊",
            "parameters": {
                "type": "object",
                "properties": {
                    "fruit_name": {
                        "type": "string",
                        "description": "指定水果名稱，可以是繁體中文或者是英文 e.g. 香蕉、banana",
                    }
                },
                "required": ["fruit_name"],
            },
        },
    }
]

response = inference(hello_message, tools)["message"]
response_with_tool = inference(tool_message, tools)["message"]
response_with_multiple_tools = inference(multiple_tool_message, tools)["message"]

print("單純聊天的回覆",response)
print("偵測到需要工具的回覆", response_with_tool)
print("偵測到需要多個工具的回覆", response_with_multiple_tools)