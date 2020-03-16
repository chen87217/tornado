# !/usr/bin/env python
# -*- coding: utf-8 -*-
__FileName__ = '__init__.py.py'
__author__ = 'chen_87217@126.com'
__date__ = '2020/3/13 0013 19:33'

import os

from tornado.web import Application

from .views import index, user
from utils.messages import MessageHandler, RobbitHandler, ChartHandler
from .views.ui import menus

BASE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
settings = {
    'debug': True,
    'template_path': os.path.join(BASE_ROOT, 'templates'),
    'static_path': os.path.join(BASE_ROOT, 'static'),
    'static_url_prefix': '/s/',
    'ui_modules':{
        'menus': menus.MenusModule
    }
}

def make_up(host):
    return Application(handlers=[
        ('/', index.IndexHandler),
        ('/user', user.UserHandler),
        ('/robbit', RobbitHandler),
        ('/message', MessageHandler),
        ('/chart', ChartHandler),
    ], default_host=host, **settings)