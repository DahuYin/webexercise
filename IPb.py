#!usr/bin/env python3
# -*- coding:utf-8 -*-

"""
test IP browser
"""

import socket


def getIp(domain):
    myaddr = socket.getaddrinfo(domain, 'http')
    print(myaddr)

if __name__ == '__main__':
    getIp('www.hust.edu.cn')

