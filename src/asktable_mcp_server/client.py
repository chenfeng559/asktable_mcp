from fastmcp import Client

async def run():
    client = Client("server.py")
    tools = await client.list_tools()
    print(tools)

if __name__ == "__main__":
    import asyncio

    asyncio.run(run())