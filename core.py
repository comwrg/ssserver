#!/usr/bin/env python
# encoding: utf-8

"""
@author: comwrg
@license: MIT
@file: core.py
@time: 2017/2/7 18:01
"""
import urllib.request
import re
import base64



def getssinfo(url = 'https://doub.io/sszhfx/'):
    with urllib.request.urlopen(url) as h:
        html = h.read().decode('utf-8')
        pattern = 'ss://(.*?)"'
        res = re.findall(pattern, html)
        configs = []
        for b64 in res:
            info = base64.b64decode(b64).decode()
            pattern = '(?P<method>.*?):(?P<password>.*)@(?P<server>.*):(?P<server_port>.*)'
            m = re.match(pattern, info)
            #print(m.groupdict())
            list = m.groupdict()
            list.setdefault('remarks', '')
            list.setdefault('auth', False)
            list.setdefault('timeout', 1)
            print(list)
            configs.append(list)
        return configs


if __name__ == '__main__':
    getssinfo()