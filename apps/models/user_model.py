from exts import My_op_db_data, db


class User(db.Model, My_op_db_data):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 主键 自增
    username = db.Column(db.String(64), nullable=False, unique=True)  # 账户
    password = db.Column(db.String(64), nullable=False)  # 密码
    phone = db.Column(db.String(11))  # 手机号 可为空
    address = db.Column(db.String(11))  # 地址 可为空

    # repr() 方法显示一个可读字符串
    def __repr__(self):
        return 'User'.format(self.username)


