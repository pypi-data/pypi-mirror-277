from msoc import search, engines
import asyncio


async def main():
    # print(await search("Sherlock"))
    async for sound in search("Его Крид"):
        print(f"Name: {sound.name}, URL: {sound.url}")


asyncio.run(main())