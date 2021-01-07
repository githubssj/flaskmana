# from flask_sqlalchemy import SQLAlchemy
#
# db = SQLAlchemy()
from flask_sqlalchemy import SQLAlchemy as BaseSQLAlchemy
from contextlib import contextmanager
from sqlalchemy.exc import IntegrityError


# 自定义一个SQLAlchemy继承flask_sqlalchemy的,方便自定义方法！！！ 为了失败回滚
class SQLAlchemy(BaseSQLAlchemy):

    # 利用contextmanager管理器,对try/except语句封装，使用的时候必须和with结合！！！
    @contextmanager
    def auto_commit_db(self):
        try:
            yield
            self.session.commit()
            self.session.remove()
        except IntegrityError as ie:
            # 加入数据库commit提交失败，必须回滚！！！
            self.session.rollback()
            self.session.remove()
            print("数据commit失败!---------auto_commit_db")
            raise ie
            # return ie


db = SQLAlchemy()


# def init_model(app):
#     db.init_app(app=app)


class My_op_db_data:
    def add_db_data(self):
        with db.auto_commit_db():
            db.session.add(self)




# 初始化 扩展
def init_exts(app):
    db.init_app(app=app)
