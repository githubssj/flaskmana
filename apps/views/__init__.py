from flask import Blueprint, render_template

index_bp = Blueprint('index', __name__)



# 成功响应
@index_bp.route('/')
def show_index():
    # return render_template('index.html')
    return "index"