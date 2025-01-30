from agent import Agent
from tools.fruit import get_fruit_info, get_remain_fruit
from prompts import (
    MULTIPLE_TOOL_SYSTEM_PROMPT,
    MULTIPLE_TOOL_USER_PROMPT
)


if __name__ == "__main__":
    fruit_agent = Agent(
        name="水果小助手",
        instructions=MULTIPLE_TOOL_SYSTEM_PROMPT,
        tools=[get_fruit_info, get_remain_fruit],
        model="gpt-4o-mini"
    )

    respnose = fruit_agent.run(MULTIPLE_TOOL_USER_PROMPT, debug=False)
    print(respnose.message.content, end="\n\n")

    respnose = fruit_agent.run("我想知道有關香蕉的所有資料，香蕉剩下多少可以買？", debug=False)
    print(respnose.message.content)