from fastmcp import Client
import asyncio
from server import mcp  
async def run():
    # 直接传递示例
    client = Client(mcp)
    async with client:
        tools = await client.list_tools()
        print(tools)

if __name__ == "__main__":
    asyncio.run(run())