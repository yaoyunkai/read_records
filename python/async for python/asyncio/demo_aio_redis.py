import aioredis
import asyncio


async def get_key(key_name):
    conn = aioredis.Redis(host='127.0.0.1', port=6379, db=5)
    res = await conn.get(key_name)
    print(res)


asyncio.run(get_key('demo'))
