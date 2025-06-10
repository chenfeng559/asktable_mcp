from fastmcp import Client
from openai import OpenAI
from typing import List, Dict


class UserClient:
    def __init__(self, script = "server.py"):
        self.mcp_client = Client(script),
        self.openai_client = OpenAI(
            base_url= "http://localhost:11434/v1",
            api_key="None"
        )
        self.tools = self.prepare_tools
    def chat(self, message : List[Dict]):
        pass

    def loop (self):
        pass

    async def prepare_tools(self):
        tools_result  = await self.mcp_client.list_tools()
        return tools_result
        