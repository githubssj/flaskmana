from flask import Blueprint, render_template

from apps.views.db_op_demo import db_op
from apps.views.login_register_view import reg_bp, login_bp
from apps.views.db_op_view import opdb_bp
from apps.views.login_test import loginT_bp
# from apps.views.require_test import reqt_bp

index_bp = Blueprint('index', __name__)


def init_view(app):
    # 注册蓝图
    app.register_blueprint(index_bp)
    app.register_blueprint(reg_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(opdb_bp)
    app.register_blueprint(loginT_bp)
    app.register_blueprint(db_op)
    # app.register_blueprint(reqt_bp)



# 成功响应
@index_bp.route('/')
def show_index():
    # return render_template('index.html')
    return "index"