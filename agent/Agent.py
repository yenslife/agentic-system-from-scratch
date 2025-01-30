from ast import Call
import inspect
import json
from typing import Callable, Any
from pydantic import BaseModel
from rich import print

from model_providers.openai import completion, CompletionResponse

class Agent(BaseModel):
    """
    基本的 Agent 元件
    """
    name: str
    instructions: str
    tools: list[Callable] = []
    model: str = "gpt-4o-mini"
    parallel_tool_calls: bool = True

    def run(self, user_input: str, debug: bool = False) -> CompletionResponse:
        messages = [
            {"role": "system", "content": self.instructions},
            {"role": "user", "content": user_input},
        ]
        tools_schema = [self._tool_to_json_schema(tool) for tool in self.tools]
        print(tools_schema) if debug else None
        return self._run(messages, tools_schema, debug)

    def _run(self, messages: str, tools_schema: list[dict], debug: bool = False) -> CompletionResponse:
        response = completion(messages, tools_schema, self.model, self.parallel_tool_calls)

        tool_calls = response.message.tool_calls or []
        if not tool_calls:
            return response

        print("Use Tool!!") if debug else None
        messages.append(response.message)  # must append model function call message
        
        for i, tool in enumerate(tool_calls):
            function_name = tool.function.name
            function_args = json.loads(tool.function.arguments)
            function_to_call = self.tools[i]
            function_response = function_to_call(**function_args)
            print(f"Function: {function_name}, Args: {function_args}, Response: {function_response}") if debug else None

            messages.append({
                "role": "tool",
                "tool_call_id": tool.id,
                "content": str(function_response)
            })

        return self._run(messages, tools_schema, debug)  # 反覆迭代

    def _tool_to_json_schema(self, func: Callable) -> dict:
        """
        將工具名稱轉換成工具 JSON schema，請參考 [Function calling](https://platform.openai.com/docs/guides/function-calling?strict-mode=enabled#strict-mode)
        TODO: 目前有一個小問題，就是函式的參數 description 沒有定義，或許可以在 tools 那邊定義一個 param 類別
        """
        type_map = {
            str: "string",
            int: "integer",
            float: "number",
            bool: "boolean",
            list: "array",
            dict: "object"
        }
        sig = inspect.signature(func)
        parameters = []
        required = []

        for param in sig.parameters.values():
            parameter = {
                "type": type_map[param.annotation],
                "name": param.name,
            }
            if param.default is not param.empty:
                parameter["default"] = param.default
            if param.annotation != param.empty:
                parameter["description"] = str(param.annotation)
            if param.default is inspect.Parameter.empty:
                required.append(parameter["name"])
            parameters.append(parameter)

        return {
            "type": "function",
            "function": {
                "name": func.__name__,
                "description": func.__doc__,
                "parameters": {
                    "type": "object",
                    "properties": {param["name"]: param for param in parameters}
                },
                "required": required
            },
        }