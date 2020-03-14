# !/usr/bin/env python
# -*- coding: utf-8 -*-
__FileName__ = 'index.py'
__author__ = 'chen_87217@126.com'
__date__ = '2020/3/13 0013 23:09'

from tornado.web import RequestHandler


class IndexHandler(RequestHandler):
    def get(self):
        data = {
            'msg': '陈乾坤',
            'item': ['陈利', '陈祥', '陈朝霞', '陈乾坤', '陈东东', '陈鹏飞'],
            'errors': '错误测试'
        }

        return self.render('index/index.html', **data)

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
