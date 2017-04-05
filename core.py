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
from ping import *


def getssinfo(url = 'https://doub.bid/sszhfx/'):
    '''
    proxy_support = urllib.request.ProxyHandler({'http' :'127.0.0.1:1080'})
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)
    '''
    with urllib.request.urlopen(url) as h:
        html = h.read().decode('utf-8')
        pattern = 'ss://(.*?==)"'
        res = re.findall(pattern, html)
        configs = []
        for b64 in res:
            info = base64.b64decode(b64).decode()
            pattern = '(?P<method>.*?):(?P<password>.*)@(?P<server>.*):(?P<server_port>.*)'
            m = re.match(pattern, info)
            #print(m.groupdict())
            listInfo = m.groupdict()
            listInfo.setdefault('remarks', '')
            listInfo.setdefault('auth', False)
            listInfo.setdefault('timeout', 1)
            print(listInfo)
            '''
            res = ping(host=list['server'], count=1, timeout=0.2)
            if res.received == 1:
                configs.append(list)
            '''
            configs.append(listInfo)
        return configs


if __name__ == '__main__':
    getssinfo()

