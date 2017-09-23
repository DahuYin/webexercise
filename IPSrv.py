#!usr/bin/env python3
# -*- coding:utf-8 -*-


"""
test IP server
"""

import socket

if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # UDP
    s.bind(('127.0.0.1', 9999))  # 绑定端口,这个端口的数据将发送过来

    # 接收数据
    while True:
        data, addr = s.recvfrom(1024)
        print('Received from{0}:{1}'.format(addr, data.decode('utf-8')))
        msgdata = b'Hello,%s!' % data
        s.sendto(msgdata, addr)
