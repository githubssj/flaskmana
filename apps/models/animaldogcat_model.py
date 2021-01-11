from exts import db, My_op_db_data


class Animal(db.Model, My_op_db_data):
    # 抽象的模型是不会在数据库中产生映射的
    __abstract__ = True  # 如果不加, 则会将继承这个类的都合并在一个表中
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    a_name = db.Column(db.String(20), nullable=True)
    c_eat = db.Column(db.String(32), nullable=True)
    d_legs = db.Column(db.Integer, nullable=True, default=4)
    e_note = db.Column(db.String(32), nullable=True)

    # repr() 方法显示一个可读字符串
    def __repr__(self):
        return 'a_name'.format(self.a_name)


class Dog(Animal):
    d_legs = db.Column(db.Integer, nullable=True, default=4)


class Cat(Animal):
    c_eat = db.Column(db.String(32), nullable=True, default="fish")
