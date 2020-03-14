# !/usr/bin/env python
# -*- coding: utf-8 -*-
__FileName__ = 'Menu.py'
__author__ = 'chen_87217@126.com'
__date__ = '2020/3/14 0014 14:52'

'''
菜单类
'''

import sqlalchemy as sql
from sqlalchemy.orm import relationship
# from sqlalchemy import Column, Integer, String, Text, ForeignKey

from utils.conn import Base

class Menu(Base):
    __tablename__ = 'menu'

    id = sql.Column(sql.Integer, primary_key=True, autoincrement=True)
    title = sql.Column(sql.String(50), unique=True, nullable=False)
    url = sql.Column(sql.String(50), default='')
    note = sql.Column(sql.Text)

    parent_id = sql.Column(sql.Integer, sql.ForeignKey('menu.id', name='parent_id_fk'))


    # childs = relationship('Menu', backref='parent')
    childs = relationship('Menu')