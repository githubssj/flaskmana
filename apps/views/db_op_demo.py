from flask import Blueprint, request, render_template
from exts import db
from apps.models.animaldogcat_model import Animal, Dog, Cat

db_op = Blueprint("db", __name__, url_prefix="/db")


@db_op.route("/addanimal/")
def add_animal():
    cat = Cat()
    cat.a_name = "加菲猫"
    cat.c_eat = "虾"
    dog = Dog()
    dog.d_legs = 5
    dog.a_name = "傻狗"
    dog.c_eat = "肉骨头"
    cat.add_db_data()
    dog.add_db_data()
    return "cat and dog add Success! "


@db_op.route("/getcats/")
def get_cats():
    cats = Cat.query.filter(Cat.id.__eq__(2))  # 这个basequery对象的__str__ 输出的是这个数据的sql脚本
    types = str(type(cats))+"啊啊啊"

    # return render_template("getcats.html", cats=cats, types=types)  # 单个参数传递和 下面的**local() 都可以
    return render_template("getcats.html", **locals())  # **local() 将所有参数传出