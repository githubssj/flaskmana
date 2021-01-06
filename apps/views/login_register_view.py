from flask import Blueprint, render_template, request, jsonify, session
from apps.models.user_model import User
from exts import db
from sqlalchemy.exc import IntegrityError

reg_bp = Blueprint('register', __name__, url_prefix="/register")
login_bp = Blueprint('login', __name__, url_prefix="/login")


# 注册路由
# 注册
@reg_bp.route("/", methods=["POST"])
def reg_index():
    try:
        my_json = request.get_json()
        # print(my_json)
        username = my_json.get("username")
        password = my_json.get("password")
        if not all([username, password]):
            return jsonify(msg="参数不完整", code=4000)
        # resp_json = {"username": username, "password":password}
        # print(resp_json)
        user = User(username=username, password=password)
        # 判断是否存在这个用户
        exists = User.query.filter_by(username=username).first()
        if exists:
            return jsonify(msg="用户"+username+"已存在", code=4003)
        # 添加到数据库, 使用exts的db 中的auto_commit_db()方法自动提交或回滚
        # User类继承了添加数据的类中的方法
        User.add_db_data(user)
        return jsonify(code=200, msg='注册成功', username=username)
    except IntegrityError as ie:  # 这是访问出错的一种方法, 还有一种为提取加验证
        print("ie:---", ie)
        return jsonify(msg="存数据库错误", code=4001)
    except Exception as e:
        print(";---------", e)
        return jsonify(msg="出错了, 请检查是否正确访问!", code=4002)


@login_bp.route("/")
def login_index():
    return "aaa"
    # return jsonify(code=200, msg='验证成功', username=username)
