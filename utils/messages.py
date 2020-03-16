# !/usr/bin/env python
# -*- coding: utf-8 -*-
__FileName__ = 'messages.py'
__author__ = 'chen_87217@126.com'
__date__ = '2020/3/15 0015 17:29'

import time
import random

from tornado.websocket import WebSocketHandler
from tornado.web import RequestHandler


class RobbitHandler(RequestHandler):
    def get(self):
        # self.render('ws/robbit.html')
        self.render('ws/chart.html')

class MessageHandler(WebSocketHandler):
    # 当前处理器是一个长连接

    def open(self): # 客户端请求连接
        ip = self.request.remote_ip

        # 向客户端发送消息
        self.write_message('你好, %s' % ip)

        for i in range(10):
            time.sleep(1)
            number = random.randint(100, 1000)
            self.write_message('%s' % number)


class ChartHandler(WebSocketHandler):
    # 当前处理器是一个长连接

    online_clients = []

    # 群发
    def group_send(self, msg):
        for client in self.online_clients:
            client.write_message(msg)

    def open(self): # 客户端请求连接
        ip = self.request.remote_ip

        self.online_clients.append(self)

        # 向客户端发送消息
        # self.write_message('你好, %s' % ip)
        # self.get_secure_cookie('').decode()

        self.group_send('你好, %s' % ip)


    def on_message(self, message):
        ip = self.request.remote_ip
        # 向客户端发送消息
        self.write_message('%s, 说:%s' % (ip, message))


