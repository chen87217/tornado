# !/usr/bin/env python
# -*- coding: utf-8 -*-
__FileName__ = 'manage.py'
__author__ = 'chen_87217@126.com'
__date__ = '2020/3/13 0013 19:32'


import tornado.ioloop
import tornado.options

from apps import make_up

if __name__ == '__main__':
    # 定义命令行参数
    tornado.options.define('port', default=8000, type=int, help="绑定socket 端口 ")
    tornado.options.define('host', default='localhost', type=str, help="设置host")

    # 解析命令行参数
    tornado.options.parse_command_line()

    host = tornado.options.options.host
    port = tornado.options.options.port

    app = make_up(host)
    app.listen(port)

    # 启动服务
    print("starting web server %s:%s" % (host, port))
    tornado.ioloop.IOLoop.current().start()