#!usr/bin/env python3
# -*- coding:utf-8 -*-

"""
WSGI test
"""


def application(environ, start_response):
    status = '200 OK'
    header = [('Content-Type', 'text/html')]
    start_response(status, header)
    body = b'<h1>hello,web!</h1>'
    return [body]


if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    httpd = make_server('', 8000, application)
    print('Serving HTTP on port 8000')
    httpd.serve_forever()
