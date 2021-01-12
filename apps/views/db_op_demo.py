import random

from flask import Blueprint, request, render_template
from exts import db, cache
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
    # 使用魔术方法__eq__来比较, 还有 __lt__ 小于等
    cats = Cat.query.filter(Cat.id.__eq__(2))  # 这个basequery对象的__str__ 输出的是这个数据的sql脚本
    # 比较 > < ==
    catsbijiao = Cat.query.filter(Cat.id == 2)
    # catsall = Cat.quert.filter(Cat.id.__eq__(2)).all()  # 这里的类型和上面不一样, 这是list
    catslt = Cat.query.filter(Cat.id.__lt__(2)).all()  # 这里的类型和上面不一样, 这是list
    types = str(type(cats))+"啊啊啊"
    print("cats:---: ", cats)
    # return render_template("getcats.html", cats=cats, types=types)  # 单个参数传递和 下面的**local() 都可以
    return render_template("getcats.html", **locals())  # **local() 将所有参数传出


# 批量添加狗
@db_op.route("/adddogs/")
def add_dogs():
    for i in range(20):
        dog = Dog()
        dog.a_name = "二哈%d" % random.randrange(10000)
        dog.add_db_data()
    return "Add dog success"


# 分页 手写简单示例
@db_op.route("/getdogspage/")
def get_dogs_page():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 4, type=int)
    dogs = Dog.query.offset(per_page * (page - 1)).limit(per_page)
    return render_template("getcats.html", **locals())


# 使用分页器 paginate  -> flaskSQlalchemy下的class BaseQuery(orm.Query): 中的paginate方法
# def paginate(self, page=None, per_page=None, error_out=True, max_per_page=None):
# @db_op.route("/getdogspaginate/", endpoint="paginationep")
@db_op.route("/getdogspaginate/")
@cache.cached(timeout=50)
def get_dogs_paginate():
    dogs = Dog.query.paginate().items  # 获取信息
    per_page = request.args.get("per_page", 4, type=int)  # 注意默认传参
    pagination = Dog.query.paginate(per_page=per_page)  # 获取迭代器
    print("从数据库中取值!------------")

    # return render_template("getcats.html", per_page=per_page, pagination=pagination, dogs = dogs)
    return render_template("getcats.html", **locals())
