#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
@author: ttlttl
@contact: wangmingape@gmail.com
@site: https://github.com/ttlttl
@file: config_default.py
@time: 9/5/2016 4:21 PM
"""


configs = {
    'debug': True,
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'aiowebapp',
        'password': 'aiowebapp',
        'db': 'aiowebapp'
    },
    'session': {
        'secret': 'aiowebapp'
    }
}
