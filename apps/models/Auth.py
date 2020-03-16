# !/usr/bin/env python
# -*- coding: utf-8 -*-
__FileName__ = 'Auth.py'
__author__ = 'chen_87217@126.com'
__date__ = '2020/3/14 0014 14:52'

from datetime import datetime

import sqlalchemy as sql
from sqlalchemy.orm import relationship
# from sqlalchemy import Column, Integer, String, Text, ForeignKey

from utils.conn import Base


class BaseModule(Base):
    '''
    系统功能表
    '''
    __tablename__ = 'base_module'
    __table_args__ = {'extend_existing': True}
    # module_id = sql.Column(sql.String(50), primary_key=True, autoincrement=True)
    module_id = sql.Column(sql.String(50), primary_key=True)
    # parent_id = sql.Column(sql.String(50), sql.ForeignKey('base_module.module_id', name='parent_id_fk'), default='')
    parent_id = sql.Column(sql.String(50), sql.ForeignKey('base_module.module_id', name='parent_id_fk'))
    encode = sql.Column(sql.String(50), comment='编码')
    # fullname = sql.Column(sql.String(50), unique=True, nullable=False, comment='标题')
    fullname = sql.Column(sql.String(50), comment='标题')
    icon = sql.Column(sql.String(50), default='', comment='图标')
    url = sql.Column(sql.String(50), default='', comment='导航地址')
    target = sql.Column(sql.String(20), comment='导航目标')
    sort = sql.Column(sql.Integer, comment='排序')

    is_menu = sql.Column(sql.BOOLEAN, comment='菜单/功能模块')
    is_allow_expand = sql.Column(sql.BOOLEAN, comment='是否展开')
    is_public = sql.Column(sql.BOOLEAN, comment='是否公开')
    meno = sql.Column(sql.String(200), comment='备注')
    add_userid = sql.Column(sql.String(50), comment='创建用户id')
    add_username = sql.Column(sql.String(50), comment='创建用户')
    add_time = sql.Column(sql.DATETIME, comment='添加时间', default=datetime.now)

    update_userid = sql.Column(sql.String(50), comment='更新用户id')
    update_username = sql.Column(sql.String(50), comment='更新用户')
    update_time = sql.Column(sql.DATETIME, comment='修改时间', default=datetime.now)

    # childs = relationship('Menu', backref='parent')
    childs = relationship('BaseModule')