最为原始的try/except办法，多次插入数据就要写多次，很麻烦，使用python原生的contextlib.contextmanager简化代码！

         try:
            user_db = User(email=self.email, nickname=self.nickname, password=self.password)
            db.session.add(user_db)
            #所有的数据处理准备好之后，执行commit才会提交到数据库！
            db.session.commit()
        except Exception as e:
            #加入数据库commit提交失败，必须回滚！！！
            db.session.rollback()
            raise e
1
2
3
4
5
6
7
8
9
最优化的一种方式，这种方法很牛逼！（对于多个try/except很好的重复性）

from flask_sqlalchemy import SQLAlchemy as BaseSQLAlchemy
from contextlib import contextmanager

#自定义一个SQLAlchemy继承flask_sqlalchemy的,方便自定义方法！！！
class  SQLAlchemy(BaseSQLAlchemy):

   #利用contextmanager管理器,对try/except语句封装，使用的时候必须和with结合！！！
   @contextmanager
   def auto_commit_db(self):
       try:
           yield
           self.session.commit()
       except Exception as e:
          # 加入数据库commit提交失败，必须回滚！！！
          self.session.rollback()
          raise e

db = SQLAlchemy()
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
利用with上下文管理方法调用！

from kirin_app.db_models.table_user import User
from kirin_app.db_models import db
 
 
class RegisterViewModel:
 
    def __init__(self,form_data):
        self.email = form_data["email"]
        self.nickname = form_data["nickname"]
        self.password = form_data["password"]
 
        self.__add_db_data()
 
    # 把数据添加进入数据库
    def __add_db_data(self):
        with db.auto_commit_db():
            user_db = User(email=self.email, nickname=self.nickname, password=self.password)
            db.session.add(user_db)
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
在这里插入图片描述