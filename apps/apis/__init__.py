# apis
from flask_restful import Api

from apps.apis.admin import admin_api
from apps.apis.myuser import user_api
from apps.apis.myuser.my_user_api import My_User_Resource




def apis_init_app(app):
    user_api.init_app(app=app)
    admin_api.init_app(app=app)


user_api.add_resource(My_User_Resource, '/userinfo/', strict_slashes=False)
