from fastmcp import Client
from openai import OpenAI
from typing import List, Dict
from server import mcp 
import asyncio
import json

class UserClient:
    def __init__(self, mcp = mcp, model = "qwen-turbo-2025-04-28"):
        self.model = model 
        self.mcp_client = Client(mcp)
        # self.openai_client = OpenAI(
        #     base_url= "http://localhost:11434/v1",
        #     api_key="None"
        # )
        self.openai_client = OpenAI(
            base_url= "https://dashscope.aliyuncs.com/compatible-mode/v1",
            api_key=""
        )
        self.tools = None  # 初始化为None，稍后异步加载
        # self.tools = self.prepare_tools
        self.messages = [
            {
                "role": "system",
                "content": "你是一个ai助手,你要根据我的问题，通过调用工具来解决我提出的问题。"

            }
        ]
    async def chat(self, message ):
        if not self.tools :
            self.tools = await self.prepare_tools()
        response = self.openai_client.chat.completions.create(
            model=self.model,
            messages=message,
            tools = self.tools,
        )

        if response.choices[0].finish_reason != "tool_calls":
            return response.choices[0].message
        
        for tool_call in response.choices[0].message.tool_calls:
            response = await self.mcp_client.call_tool(
                tool_call.function.name, json.loads(tool_call.function.arguments)
                )
            
            self.messages.append({
                "role": "assistant",
                "content": response[0].text
            })

            return await self.chat(self.messages)

        print("this chat response",response)

    async def loop (self):
        # qwen2.5:7b 
        async with self.mcp_client:
            while(True):
                question = input("user: ")
                message = {
                    "role": "user",
                    "content": question
                }
                self.messages.append(message)
                response_message = await self.chat(self.messages)
                if response_message is not None:
                    print("assistant: ", response_message.content)
                else :
                    print("assistant: ", "连接失败。")
        

    async def prepare_tools(self):
        tools_result  = await self.mcp_client.list_tools()

        tools = [
            {
                "type": "function",
                "function": {
                    "name": tool.name,
                    "description": tool.description,
                    "input_schema": tool.inputSchema
                    }
                
            }
            for tool in tools_result
        ]
        # print(tools)
        return tools
    
async def main():
    user_client = UserClient()
    await user_client.loop()
        
if __name__ == "__main__":
    asyncio.run(main())
    