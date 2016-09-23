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
    summary = 'hello world, good good study'
    blogs = [
        Blog(id='1', name="Test1", summary=summary, created_at=time.time() - 120),
        Blog(id='2', name="Test2", summary=summary, created_at=time.time() - 1200),
        Blog(id='3', name="Test3", summary=summary, created_at=time.time() - 2400),
        Blog(id='4', name="Test4", summary=summary, created_at=time.time() - 3600),
    ]
    return {
        '__template__' : 'blogs.html',
        'blogs' : blogs
    }


@get('/api/users')
async def api_get_users():
    users = await User.findAll(orderBy='created_at desc')
    for u in users:
        u.password = '*********'
    return dict(users=users)