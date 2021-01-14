from flask import Flask, g

from apps.apis import apis_init_app
from exts import init_exts
from settings import config_map
from apps.views import index_bp, init_view
# 示例
# from apps.views.blog_view import blog_bp
# from apps.views.house_view import house_bp
# 正式
from apps.views.login_register_view import reg_bp, login_bp


# from exts import db


def create_app(config_name=config_map.get('develop')):
    # 创建 flask对象
    app = Flask(__name__, template_folder='../template')
    # 设置flask的配置
    app.config.from_object(config_name)


    # print(app.config)
    # db与app的初始化
    # db.init_app(app=app)
    # 改用 init_model(app) 懒加载
    # init_model(app=app)  # 以后从exts中导入init_exts(app) 来初始化扩展
    init_exts(app)
    # 初始化views 懒加载app的方式
    init_view(app=app)
    apis_init_app(app=app)

    # # 注册蓝图, 这些功能放到views中的init 懒加载app
    # app.register_blueprint(index_bp)
    # 示例
    # app.register_blueprint(house_bp, url_prefix='/houses')  # 这里再写url_prefix 会覆盖蓝图文件中写的默认值, 注意要加/
    # app.register_blueprint(blog_bp)
    # 正式
    # app.register_blueprint(reg_bp)
    # app.register_blueprint(login_bp)

    return app
