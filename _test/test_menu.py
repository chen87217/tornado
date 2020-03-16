# !/usr/bin/env python
# -*- coding: utf-8 -*-
__FileName__ = 'test_menu.py'
__author__ = 'chen_87217@126.com'
__date__ = '2020/3/14 0014 15:51'

from unittest import TestCase

from utils.conn import Base, session
from apps.models.Auth import BaseModule


class TestMenu(TestCase):
    # def tet_clear_mapping(self):
    #     Base.metadata.clear()

    def test_craete_table(self):
        Base.metadata.drop_all()
        Base.metadata.create_all()

    # def test_add(self):
    #     menu = BaseModule()
    #     menu.title = '测试'
    #     session.add(menu)
    #     session.commit()
    #
    # def test_mul_add(self):
    #     session.add_all([
    #         Menu(title='仓库管理'),
    #         Menu(title='商品管理', url='/goods', parent_id=2),
    #         Menu(title='入库作业', url='/in', parent_id=2),
    #         Menu(title='出库作业', url='/out', parent_id=2),
    #         Menu(title='报表统计'),
    #         Menu(title='个人中心')
    #     ])
    #     session.commit()
    #
    # def test_get(self):
    #     # 查询 session.query(模型类)
    #     m = session.query(Menu).get(2)
    #     print(m.title)
    #     for c in m.childs:
    #         print(c.title)
    #
    # def test_filter_get(self):
    #     menus = session.query(Menu).filter(Menu.parent_id.is_(None)).all()
    #     for m in menus:
    #         print(m.title)
    #         for c in m.childs:
    #             print('-'*5, c.title)
    #
    #
    # def test_update(self):
    #     menu = session.query(Menu).get(1)
    #     menu.title = '设置'
    #     session.commit()
    #
    #     """更新数据，默认开启事务"""
    #     # session.query(User).filter(User.username == 'jack').update({User.username: 'xiaoming'})
    #     # session.commit()
    #
    #
    # def test_remove(self):
    #     menu = session.query(Menu).filter(Menu.title == '测试').first()
    #     if menu is not None:
    #         session.delete(menu)
    #         session.commit()
    #         print('删除成功')
    #     else:
    #         print('对象不存在')