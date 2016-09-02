#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: ttlttl
@contact: wangmingape@gmail.com
@site: https://github.com/ttlttl
@file: app.py.py
@time: 9/1/2016 2:00 PM
"""


import logging
import asyncio
from aiohttp import web

logging.basicConfig(level=logging.INFO)


def index(request):
    return web.Response(body=b'<h1>hello, aiohttp</h1>')


async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    server = await loop.create_server(app.make_handler(), '127.0.0.1', 5000)
    logging.info('Server started on 127.0.0.1:5000...')
    return server


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
