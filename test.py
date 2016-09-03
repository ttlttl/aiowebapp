#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: ttlttl
@contact: wangmingape@gmail.com
@site: https://github.com/ttlttl
@file: test.py.py
@time: 9/2/2016 3:17 PM
"""


import asyncio
import orm
from models import User
import sys


async def test(loop):
    await orm.create_pool(loop=loop, host='192.168.111.10', user='aiowebapp', password='aiowebapp', db='aiowebapp')
    u = User(name='Test', email='test@example.com', passwd='1234567890', image='#')
    await u.save()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.close()
    if loop.is_closed():
        sys.exit(0)