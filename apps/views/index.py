# !/usr/bin/env python
# -*- coding: utf-8 -*-
__FileName__ = 'index.py'
__author__ = 'chen_87217@126.com'
__date__ = '2020/3/13 0013 23:09'

from tornado.web import RequestHandler

from models.Auth import BaseModule
from utils.conn import session

class IndexHandler(RequestHandler):
    def get_menus(self, module_id=''):
        if module_id == '':
            menus = session.query(BaseModule).filter(BaseModule.parent_id.is_(None)).all()
        else:
            menus = session.query(BaseModule).filter(BaseModule.module_id == module_id).first()
        return menus


    def get(self):
        modules = self.get_menus()
        data = {
            'msg': '陈乾坤',
            'item': ['陈利', '陈祥', '陈朝霞', '陈乾坤', '陈东东', '陈鹏飞'],
            'errors': '错误测试',
            'modules': modules
        }

        return self.render('index/index.html', **data)

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
