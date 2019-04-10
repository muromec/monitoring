import asyncio
from aiohttp import web, WSMsgType

def index(request):
    with open('templates/index.html') as template:
        return web.Response(
                text=template.read(),
                content_type='text/html'
        )

brew = {
}

async def socket(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    brew['only'] = ws

    while True:
        await asyncio.sleep(1)

async def inlet(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    while True:
        msg = await ws.receive()
        if msg.type != WSMsgType.TEXT: break

        if 'only' in brew:
            await brew['only'].send_str(msg.data)

    return ws


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    aio_app = web.Application()
    aio_app.router.add_static('/static', './static/')
    aio_app.router.add_route('GET', '/', index)
    aio_app.router.add_route('GET', '/socket', socket)
    aio_app.router.add_route('GET', '/inlet', inlet)
    web.run_app(aio_app, port=5555)
