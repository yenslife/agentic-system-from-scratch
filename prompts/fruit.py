# 單純與模型聊天的 message
hello_message = [
    {"role": "system", "content": "你是資料庫查詢機器人，使用繁體中文回答使用者的問題"},
    {"role": "user", "content": "你好哇！可以自我介紹一下嗎？"}
]

# 需要使用單一工具的 message
tool_message = [
    {"role": "system", "content": "你是資料庫查詢機器人，使用繁體中文回答使用者的問題"},
    {"role": "user", "content": "我想查詢蘋果剩下多少個"}
]

# 需要使用多個工具的 message
multiple_tool_message = [
    {"role": "system", "content": "你是資料庫查詢機器人，使用繁體中文回答使用者的問題"},
    {"role": "user", "content": "我想查詢蘋果的資料，順便看看香蕉剩下多少"}
]