from flask import Blueprint, request
from exts import db
from apps.models.user_model import User

opdb_bp = Blueprint("opdb", __name__)

@opdb_bp.route("/createdb/")
def createdb():
    db.create_all()
    return "creatdb success"


@opdb_bp.route("/dropdb/")
def dropdb():
    db.drop_all()
    return "dropdb success"


@opdb_bp.route("/adduser/", methods=["GET", "POST"])
def adduser():
    if request.method == "GET":
        getargs = request.args.get("username")
        print(getargs)
        return "GET username=" + getargs
    elif request.method == "POST":
        my_json: dict = request.get_json()
        username = my_json.get("username")
        password = my_json.get("password")
        user = User()
        user.username = username
        user.password = password
        user.add_db_data()
        return "POST username & password 添加成功"