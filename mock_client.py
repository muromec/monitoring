import asyncio
import aiohttp

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.ws_connect('http://localhost:5555/inlet') as ws:
            for n in range(20):
                await ws.send_str(str(n))
                await asyncio.sleep(1.0)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
