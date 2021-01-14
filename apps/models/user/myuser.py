from werkzeug.security import generate_password_hash, check_password_hash

from apps.models import BaseModel
from exts import db
from apps.models.user.model_constant import PERMISSION_NONE


"""
username password phone email is_del permission
权限设计使用linux式的 rwx 读写执行 421 100 010 001
"""


class MyUser(BaseModel):

    __tablename__ = "myuser"
    username = db.Column(db.String(32), nullable=False, unique=True)
    _password = db.Column(db.String(256), nullable=False)  # 内部字段 设置property
    phone = db.Column(db.String(32), unique=True)
    is_del = db.Column(db.Boolean, nullable=False, default=False)
    active = db.Column(db.Boolean, nullable=False, default=False)
    permission = db.Column(db.Integer, default=PERMISSION_NONE)

    @property
    def password(self):
        raise Exception(" can't access! ")

    @password.setter
    def password(self, password_val):
        self._password = generate_password_hash(password_val)

    # 校验密码
    def check_password(self, password_val):
        return check_password_hash(self._password, password=password_val)
