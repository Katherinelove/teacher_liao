# -*- coding: utf-8 -*-

"""
如果把一个tuple(关系数据库表中的一行字段)用class实例属性来表示，就可以更容易地看出表的结构来：
这就是传说中的ORM技术：Object-Relational Mapping，把关系数据库的表结构映射到对象上。是不是很简单？
但是由谁来做这个转换呢？所以ORM框架应运而生。
在Python中，最有名的ORM框架是SQLAlchemy。我们来看看SQLAlchemy的用法
可见，ORM就是把数据库表的行与相应的对象建立关联，互相转换。
由于关系数据库的多个表还可以用外键实现一对多、多对多等关联，相应地，ORM框架也可以提供两个对象之间的一对多、多对多等功能.
ORM框架的作用就是把数据库表的一行记录与一个对象互相做自动转换。

第一步，导入SQLAlchemy，并初始化DBSession：
"""

__author__ = 'katherinelove'

from sqlalchemy import Column,String,VARCHAR,INT,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql

# 创建对象的基类:
base = declarative_base()
# 定义User对象:
class User(base):
    #表的名字
    __tablename__="student"

    # 表的结构:
    id=Column(String(4),primary_key=True)
    name=Column(String(12))
    phone=Column(String(11))
    email=Column(String(32))


def writeIn():
    # 由于有了ORM，我们向数据库表中添加一行记录，可以视为添加一个User对象：
    # 创建session对象:
    session = DBSession()
    # 创建新User对象:
    user1 = User(id=4, name="吴越", phone="13423010409", email="ll@163.com")
    # 添加到session:
    session.add(user1)
    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()


def queryOut():
    # 查询数据内容，以对象形式显示
    # 创建Session:
    session1 = DBSession()
    # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
    user2 = session1.query(User).filter(User.id == "1").one()  # 注意是 判断 ==
    print(user2.id, user2.name, user2.phone, user2.email)
    session1.close()

def queryAll():
    session=DBSession()
    users=session.query(User).all()
    for user in users:
        print(user.id, user.name, user.phone, user.email)
    session.close()

if __name__ == '__main__':
    # 初始化数据库连接:
    engine=create_engine("mysql+pymysql://root:123456@localhost:3306/student")
    ###create_engine()用来初始化数据库连接。SQLAlchemy用一个字符串表示连接信息：
    ###'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
    # 创建DBSession类型:
    DBSession = sessionmaker(bind=engine)

    # writeIn()
    # queryOut()
    queryAll()