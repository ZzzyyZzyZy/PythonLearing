# coding:utf-8
"""
desc: WSGI服务器实现
"""
from wsgiref.simple_server import make_server


def hello(environ, start_response):
    status = "200 OK"
    response_headers = [('Content-Type', 'text/html')]
    start_response(status, response_headers)
    path = environ['PATH_INFO'][1:] or 'hello'
    return [b'<h1> %s </h1>' % path.encode()]


def main():
    server = make_server('localhost', 8001, hello)
    print('Serving HTTP on port 8001...')
    server.serve_forever()


if __name__ == '__main__':
    main()