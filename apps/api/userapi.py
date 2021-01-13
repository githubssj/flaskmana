from flask import request
from flask_restful import Resource



class UsersResource(Resource):

    def get(self):
        return {"Users列表": "列表内容"}

    def post(self):
        return {"Users列表": "post ok"}

class UserResource(Resource):
    def get(self, id):
        print("request----:", *request.args)
        return {"单个user": id}



