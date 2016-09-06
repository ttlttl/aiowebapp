#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: ttlttl
@contact: wangmingape@gmail.com
@site: https://github.com/ttlttl
@file: handlers.py
@time: 9/5/2016 3:37 PM
"""


import re, time, json, logging, hashlib, base64, asyncio
from coroweb import get, post
from models import User, Comment, Blog, default_id


@get('/')
async def index(request):
    users = await User.findAll()
    return {'__template__': 'test.html', 'users': users}
