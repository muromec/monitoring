import json
import random
import asyncio
import aiohttp

def single_param_generator(initial, lower_rand, higher_rand):
    yield initial

    step = initial
    def next_step():
        return step + (random.randint(lower_rand, higher_rand) / 100.0)

    while True:
        step = next_step()
        yield step

def param_generators(config):
    generators = {
        key: single_param_generator(*args)
        for key, args in config.items()
    }
    while True:
        params = {
            key: next(generator_fn)
            for key, generator_fn in generators.items()
        }
        yield params

PARAM_STEPS_CONFIG = {
    'ph': [7.0, -2, 0],
    'color': [0, 0, 50],
    'bitterness': [0, 0, 20],
    'turbidity': [0, 0, 20],
    'alcohol': [0, 0, 5],
    'attenuation': [0, 0, 30],
    'gravity': [1, 0, 1],
}

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.ws_connect('http://localhost:5555/inlet') as ws:
            for param in param_generators(PARAM_STEPS_CONFIG):
                await ws.send_str(json.dumps(param))
                await asyncio.sleep(1.0)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
