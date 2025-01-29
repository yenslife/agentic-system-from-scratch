def get_remain_fruit(fruit_name: str):
    """回傳剩餘水果數量"""
    if fruit_name == "香蕉" or fruit_name == "banana":
        return 10
    elif fruit_name == "蘋果" or fruit_name == "apple":
        return 12
    else:
        return -1  # not founds

def get_fruit_info(fruit_name: str):
    """回傳水果的詳細資訊"""
    if fruit_name == "香蕉" or fruit_name == "banana":
        return {
            "name": "香蕉",
            "price": 10,
        }
    elif fruit_name == "蘋果" or fruit_name == "apple":
        return {
            "name": "蘋果",
            "price": 12,
        }
    else:
        return -1  # not founds