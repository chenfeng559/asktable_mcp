from fastmcp import Client
import asyncio
async def run():
    client = Client("server.py")
    async with client:
        tools = await client.list_tools()
        print(tools)

if __name__ == "__main__":
    asyncio.run(run())