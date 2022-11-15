'''
Author: J.sky bosichong@qq.com
Date: 2022-11-15 08:43:07
LastEditors: J.sky bosichong@qq.com
LastEditTime: 2022-11-15 09:12:13
FilePath: /sqlalchemy-test/crud.py
Description: crud工具 少年，我看你骨骼精奇，是万中无一的编程奇才，有个程序员大佬qq群[217840699]你加下吧!维护世界和平就靠你了
'''

from sqlalchemy.orm import Session
from models import *


def get_user(db:Session,username:str): 
    return db.query(User).filter(User.username==username).first()

def get_users(db:Session,skip:int = 0,limit:int=100):
    return db.query(User).all()

def get_articles(db:Session,skip:int = 0,limit:int=10):
    return db.query(Article).offset(skip).limit(limit).all()
