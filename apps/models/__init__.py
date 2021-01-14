# models的init文件
# 定义一个基础虚拟类
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.util.compat import contextmanager

from exts import db


class BaseModel(db.Model):
    __abstract__ = True
    # 定义主键id
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)

    # 保存数据方法
    def save_normal(self):
        try:
            db.session.add(self)
            db.session.commit()
            """
            我现在的需求是：从数据库中查询得到了一个对象实例之后，
            就想让这个对象与数据库切断联系，SQLAlchemy有提供这样的方法吗？
            我必须定义一个具有同样成员的类然后再初始化它？
            貌似
                db.session.refresh(self)  # 为了读取自增字段值(如果有的话)到对象
                db.session.expunge(self)   就是干这事的!!
            """
            db.session.refresh(self)
            db.session.expunge(self)

            return True
        except Exception as e:
            print("Exception Info: %s" % e)
            return False
        finally:
            db.session.close()

    # 正式使用的保存方法
    def save(self):
        """
        正式使用的保存方法
        :return:
        """
        db.session.add(self)
        return session_commit()

    # 更新数据方法
    def update_normal(self):
        try:
            db.session.commit()

            return True
        except Exception as e:
            print("Exception Info: %s" % e)
            return False
        finally:
            db.session.close()

    # 正式使用的更新方法
    def update(self):
        """
        正式使用的更新方法
        :return:
        """
        return session_commit()

    # 删除
    # 删除数据方法
    def delete_normal(self):
        try:
            db.session.delete(self)
            db.session.commit()

            return True
        except Exception as e:
            print("Exception Info: %s" % e)
            return False
        finally:
            db.session.close()

    # 正式使用的删除方法
    def delete(self):
        """
        正式使用的删除方法
        :return:
        """
        db.session.delete(self)
        return session_commit()


def session_commit():
    try:
        db.session.commit()
        return True,
    except SQLAlchemyError as e:
        db.session.rollback()
        reason = str(e)
        print("commit err reason:  %s " % reason)
        return False, reason


"""
示例:
def session_commit():
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        reason = str(e)
        return reason
"""
