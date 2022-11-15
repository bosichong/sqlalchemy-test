'''
Author: J.sky bosichong@qq.com
Date: 2022-11-14 20:40:52
LastEditors: J.sky bosichong@qq.com
LastEditTime: 2022-11-15 09:12:44
FilePath: /sqlalchemy-test/test_db.py
少年，我看你骨骼精奇，是万中无一的编程奇才，有个程序员大佬qq群[217840699]你加下吧!维护世界和平就靠你了
'''


import pytest

from database import get_db,Base,engine
from models import User,UserData,Article,Tag
from crud import *



class TestSqlAlchemy: 
    def setup_class(self):
        print('少年，我看你骨骼精奇，是万中无一的编程奇才，有个程序员大佬qq群[217840699]你加下吧!维护世界和平就靠你了')
        self.db = get_db()
        Base.metadata.create_all(engine)
        print('创建数据库表')

    
    def test_1to1(self):
        user = User(username='haha')
        self.db.add(user)
        self.db.commit()
        userdata = UserData()
        userdata.user = user
        userdata.email = 'haha@qq.com'
        # userdata.user_id = user.id #建立关系方法1
        userdata.user = user  # 建立关系方法2
        self.db.add(userdata)
        self.db.commit()
        c = self.db.query(User).count()
        print(user.username,userdata.email)
        assert c > 0

        
    def test_1tomore(self):
        article = Article(title='aaa', description='这是一段description', body='很长一段的文章啦!' )
        user = self.db.query(User).filter(User.username == 'haha').first()
        article.user_id = user.id #建立关系方法1
        article1 = Article(title='ggg', description='这是一段description', body='很长一段的文章啦!')
        article1.user = user  # 建立关系方法2
        # user.articles.append(artilce) #建立关系方法3
        self.db.add(article)
        self.db.add(article1)
        self.db.commit()
        print(article.title,article.description,article.body)
        c = self.db.query(Article).count()
        assert c > 0

    def test_moretomore(self):
        user = self.db.query(User).filter(User.username == 'haha').first()
        # 闯将文章
        art1 = Article(title='我是王大锤',user_id=user.id)
        art2 = Article(title='小狗露西很可爱',user_id=user.id)
        art3 = Article(title='快乐的写代码',user_id=user.id)
        # 闯将分类
        tag1 = Tag(name='分类1')
        tag2 = Tag(name='分类2')
        # 归类文章
        tag1.articles.append(art1)
        tag1.articles.append(art2)
        tag2.articles.append(art2)
        tag2.articles.append(art3)
        # 添加数据
        self.db.add(art1)
        self.db.add(art2)
        self.db.add(art3)
        self.db.add(tag1)
        self.db.add(tag2)
        self.db.commit()
        # 测试打印结果

        for a in tag1.articles:
            print(a.title)

        for t in art2.tags:
            print(t.name)

    def test_crud(self):
        user = get_user(self.db,'haha')
        assert user.username == 'haha'
        users = get_users(self.db)
        assert len(users) == 1
        arts = get_articles(self.db)
        assert len(arts) == 5
    
    def teardown_class(self):
        Base.metadata.drop_all(engine)
        print('删除说有数据库表')

if __name__ == '__main__':
    pytest.main(["-vs", "test_db.py"])