#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
test
"""


def reader():
    data_out = 0
    data_in = 0

    for i in range(4):
        data_in = yield data_out


def reader_wrapper(g):
    yield from g  # 等价于  for v in g: yield g


if __name__ == '__main__':

    read = reader()
    wrap = reader_wrapper(read)

    # 发送和接收数据
    r1 = wrap.send(None)  # 生成器准备好接收数据
    print(r1)
    r2 = wrap.send(1)  # send(...)数据到data_in,循环一次后,data_out传给r2
    print(r2)

    wrap.close()
