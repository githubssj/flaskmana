# from flask_sqlalchemy import SQLAlchemy
#
# db = SQLAlchemy()
from flask_caching import Cache
from flask_debugtoolbar import DebugToolbarExtension
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy as BaseSQLAlchemy
from contextlib import contextmanager
from sqlalchemy.exc import IntegrityError
from redis import Redis

from apps.api import restapi

"""
配置区
"""
# flask-caching 配置
flaskcaching_config = {
    "DEBUG": True,  # some Flask specific configs
    "CACHE_TYPE": "redis",  # Flask-Caching related configs  : simple redis
    "CACHE_DEFAULT_TIMEOUT": 300
}
cache = Cache(config=flaskcaching_config)


# 自定义一个SQLAlchemy继承flask_sqlalchemy的,方便自定义方法！！！ 为了失败回滚
class SQLAlchemy(BaseSQLAlchemy):

    # 利用contextmanager管理器,对try/except语句封装，使用的时候必须和with结合！！！
    @contextmanager
    def auto_commit_db(self):
        try:
            yield
            self.session.commit()
            return True
        except IntegrityError as ie:
            # 加入数据库commit提交失败，必须回滚！！！
            self.session.rollback()
            # self.session.remove()  # 这个使用要注意
            print("error: ", ie)
            print("数据commit失败!---------auto_commit_db")
            return False
            # raise ie
            # return ie
        finally:
            self.session.close()

    def add_db_data(self):
        with self.auto_commit_db():
            self.session.add()


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
    Session(app)
    DebugToolbarExtension(app=app)
    cache.init_app(app=app)
    restapi.init_app(app=app)
