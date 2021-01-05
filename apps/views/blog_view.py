from flask import Blueprint, render_template

blog_bp = Blueprint('blog', __name__, url_prefix='/blog')  # __name__ 表示当前文件名

# 注册路由
@blog_bp.route('/')
def blog_index():
    return 'blog 首页'
