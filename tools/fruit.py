from openai import OpenAI
from dotenv import load_dotenv

# set ENV variables
load_dotenv()
client = OpenAI()

# tool function
def get_remain_fruit(fruit_name: str):
    """回傳剩餘水果數量"""
    if fruit_name == "香蕉" or fruit_name == "banana":
        return 10
    elif fruit_name == "蘋果" or fruit_name == "apple":
        return 12
    else:
        return -1  # not founds