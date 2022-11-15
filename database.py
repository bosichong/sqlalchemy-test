'''
Author: J.sky bosichong@qq.com
Date: 2022-11-14 08:55:37
LastEditors: J.sky bosichong@qq.com
LastEditTime: 2022-11-15 09:12:21
FilePath: /sqlalchemy-test/database.py
Description: 少年，我看你骨骼精奇，是万中无一的编程奇才，有个程序员大佬qq群[217840699]你加下吧!维护世界和平就靠你了
'''
# -*- coding: UTF-8 -*-

import os,sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

# 组装数据库的绝对地址
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(BASE_DIR, 'data.db')
# 数据库访问地址
SQLALCHEMY_DATABASE_URL = "sqlite:///" + DB_DIR
# print(SQLALCHEMY_DATABASE_URL)

# 创建SQLite数据库
# engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=False)
# 创建一个使用内存的SQLite数据库
engine = create_engine("sqlite+pysqlite:///:memory:", echo=False, future=True)

# 数据模型的基类
Base = declarative_base()

# 启动会话
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# print(engine)
# print(Base)
# print(SessionLocal)

# 获取一个数据连接 异步 fastapi下使用.
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# 获取一个数据连接 
def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()


if __name__ == '__main__':
    db = get_db()
    print(dir(db))