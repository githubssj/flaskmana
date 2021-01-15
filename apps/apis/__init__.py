# apis
from flask_restful import Api

from apps.apis.admin import admin_api
from apps.apis.myuser import user_api
from apps.apis.myuser.my_user_api import My_User_Resource
from apps.apis.myuser.require_test import ReqTResource


def apis_init_app(app):
    user_api.init_app(app=app)
    admin_api.init_app(app=app)


user_api.add_resource(My_User_Resource, '/userinfo/', strict_slashes=False)
user_api.add_resource(ReqTResource, '/reqt/', strict_slashes=False)
