# !/usr/bin/env python
# -*- coding: utf-8 -*-
__FileName__ = 'conn.py'
__author__ = 'chen_87217@126.com'
__date__ = '2020/3/14 0014 14:42'


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# mysql数据库配置
settings = {
    'HOST': '127.0.0.1',
    'PORT': 3308,
    'DATABASE': 'tornadodb',
    'USERNAME': 'root',
    'PASSWORD':  '',
    'CHARSET': 'utf8',
}

engine = create_engine("mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset={charset}" \
    .format(username=settings['USERNAME'], password=settings['PASSWORD'], host=settings['HOST'], port=settings['PORT'], db=settings['DATABASE'], charset=settings['CHARSET'])
)

# 生成数据库连接
DbSession = sessionmaker(bind=engine)

# 创建会话类对象
session = DbSession()

# 生成所有模型类的父类
Base = declarative_base(bind=engine)