from rich import print

from tools.fruit import get_remain_fruit
from model_providers.openai import inference

# 定義工具
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
    }
]

# 單純與模型聊天的 message
messages = [
    {"role": "system", "content": "你是資料庫查詢機器人，使用繁體中文回答使用者的問題"},
    {"role": "user", "content": "你好哇！可以自我介紹一下嗎？"}
]

# 需要使用工具的 message
tool_message = [
    {"role": "system", "content": "你是資料庫查詢機器人，使用繁體中文回答使用者的問題"},
    {"role": "user", "content": "目前還剩下多少香蕉？"}
]

response = inference(messages, tools)["response"]
response_with_tool = inference(tool_message, tools)["response"]

print("單純聊天的回覆",response)
print("偵測到需要工具的回覆", response_with_tool)
