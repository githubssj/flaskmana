from flask import render_template

from settings import config_map
from apps import create_app

app = create_app(config_map.get('develop'))


# 这下面的默认 / 首页 放到apps/views/__init__.py中
# @app.route('/')
# def show_index():
#     return render_template('index.html')

if __name__ == '__main__':
    print(app.url_map)
    app.run()