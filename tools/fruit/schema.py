FRUIT_FUNCTION_SCHEMA = {
    "get_remain_fruit": {
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
    "get_fruit_info": {
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
}
