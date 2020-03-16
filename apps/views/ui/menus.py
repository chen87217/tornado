# !/usr/bin/env python
# -*- coding: utf-8 -*-
__FileName__ = 'menus.py'
__author__ = 'chen_87217@126.com'
__date__ = '2020/3/15 0015 22:25'

from tornado.web import UIModule


class MenusModule(UIModule):
    def render(self, modules):
        data = {
            'modules': modules
        }
        return self.render_string('ui/menus.html', **data)
