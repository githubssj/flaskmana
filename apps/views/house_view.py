from flask import Blueprint

house_bp = Blueprint('house', __name__, url_prefix='/house')  # '/house 是url_prefix

# 注册house的路由
@house_bp.route('/', endpoint='index')
def house_index():
    return '房产首页'