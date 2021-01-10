from flask import Blueprint, request, render_template, Response, session

loginT_bp = Blueprint("logintest", __name__, url_prefix="/logintest")

@loginT_bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("logintest.html")
    elif request.method == "POST":
        username = request.form.get("username")
        # 存入cookies
        response = Response("登录成功 %s " % username)
        # return "Login Test Index:  %s" % username
        # 存储到cookies中
        # response.set_cookie("username", username)
        # 存储到session中
        session['username'] = username
        return response

@loginT_bp.route("/getcookie")
def get_cookies():
    # 通过cokkies获取
    # username = request.cookies.get("username")
    # 通过session获取
    username = session.get('username')
    return "欢迎回来 %s" % username