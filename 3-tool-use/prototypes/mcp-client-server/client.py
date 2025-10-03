import json
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client

server_params = StdioServerParameters(
    command="python",
    args=["weather/weather.py"],
    env=None)

async def handle_sampling_message(
        message: types.CreateMessageRequestParams)\
        -> types.CreateMessageResult:
    return types.CreateMessageResponse(
        role="assistant",
        content=types.TextContent(
            type="text",
            text=f"Hello world! (from model)"))

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(
                read_stream=read,
                write_stream=write,
                sampling_callback=handle_sampling_message) as session:

            await session.initialize()

            # prompts = await session.list_prompts()
            #
            # prompt = await session.get_prompt(
            #     name="example-prompt",
            #     arguments={"arg1": "value1"})

            resources = await session.list_resources()

            tools = await session.list_tools()

            print("# Resources:")
            print(resources)
            print()
            print("# Tools:")
            print(tools)

if __name__ == "__main__":
    import asyncio
    asyncio.run(run())

