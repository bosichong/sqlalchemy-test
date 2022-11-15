'''
Author: J.sky bosichong@qq.com
Date: 2022-11-14 15:49:53
LastEditors: J.sky bosichong@qq.com
LastEditTime: 2022-11-15 09:12:31
FilePath: /sqlalchemy-test/models.py
Description: 少年，我看你骨骼精奇，是万中无一的编程奇才，有个程序员大佬qq群[217840699]你加下吧!维护世界和平就靠你了
'''
from database import Base
from sqlalchemy import String, Column, Integer, DateTime, Enum, Table, ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False, index=True)
    # user 一对一 UserData
    userdata = relationship('UserData',uselist=False,back_populates='user')
    # user 一对多 Article
    articles = relationship('Article',uselist=True,back_populates='user')

class UserData(Base):
    __tablename__ = 'userdata'
    id = Column(Integer, primary_key=True)
    email = Column(String(100), nullable=False)
    # user 一对一 UserData
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User', back_populates='userdata')

# article 多对多 tag 关系表
class article_tag(Base):
    __tablename__ = 'article_tag'
    id = Column(Integer, primary_key=True)
    article_id = Column(Integer, ForeignKey('article.id'), nullable=False)
    tag_id = Column(Integer, ForeignKey('tag.id'), nullable=False)


class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    # tag 多对多 article
    articles = relationship('Article', back_populates='tags',secondary='article_tag')
    

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(String(200))
    body = Column(String(200))
    # user 一对多 Article
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User', back_populates='articles')
    # tag 多对多 article
    tags = relationship('Tag',back_populates='articles',secondary='article_tag')



'''
backref

​ 替换了原来的参数，变为了一个属性参数，并使反向关系的结果也成为一个query对象，支持继续查询过滤

secondary

​ 用来指明中间的关系表，构建额外多对多关系的表

primaryjoin

​ 多对多中用于从子对象查询其父对象的 condition（child.parents），默认只考虑外键

secondaryjoin

​ 多对多中用于从父对象查询其所有子对象的 condition（parent.children），同样的，默认情况下只考虑外键


'''