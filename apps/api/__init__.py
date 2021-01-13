from flask_restful import Api

from apps.api.userapi import UsersResource, UserResource

restapi = Api()


def init_api(app):
    restapi.init_app(app=app)


# flask-restful 注册资源
restapi.add_resource(UsersResource, "/usersapi/", strict_slashes=False)
restapi.add_resource(UserResource, "/userapi/<int:id>", strict_slashes=False)
