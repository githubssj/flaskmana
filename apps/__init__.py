from flask import Flask

from settings import config_map
from apps.views import index_bp
# 示例
# from apps.views.blog_view import blog_bp
# from apps.views.house_view import house_bp
# 正式
from apps.views.login_register_view import reg_bp, login_bp
from exts import db


def create_app(config_name=config_map.get('develop')):
    # 创建 flask对象
    app = Flask(__name__, template_folder='../template')
    # 设置flask的配置
    app.config.from_object(config_name)
    # print(app.config)
    # db与app的初始化
    db.init_app(app=app)

    # 注册蓝图
    app.register_blueprint(index_bp)
    # 示例
    # app.register_blueprint(house_bp, url_prefix='/houses')  # 这里再写url_prefix 会覆盖蓝图文件中写的默认值, 注意要加/
    # app.register_blueprint(blog_bp)
    # 正式
    app.register_blueprint(reg_bp)
    app.register_blueprint(login_bp)

    return app