"""Simple demo of using Flask with aiohttp via aiohttp-wsgi's
WSGIHandler.
"""

import asyncio
from aiohttp import web
from aiohttp_wsgi import WSGIHandler
from flask import Flask, render_template

app = Flask('aioflask')
app.config['DEBUG'] = True


@app.route('/')
def index():
    return render_template('index.html')

async def socket(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)
    await ws.receive()

    for x in range(2):
        try:
            await ws.send_str(str(x))
        except:
            pass
        await asyncio.sleep(1)

    return ws


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    aio_app = web.Application()
    wsgi = WSGIHandler(app)
    aio_app.router.add_route('*', '/{path_info: *}', wsgi.handle_request)
    aio_app.router.add_static('/static', './static/')
    aio_app.router.add_route('GET', '/socket', socket)
    web.run_app(aio_app, port=5555)
