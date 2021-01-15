from flask_restful import reqparse, Resource

parse = reqparse.RequestParser()
parse.add_argument("token", required=True, help="请登录")


class ReqTResource(Resource):

    def get(self):
        args = parse.parse_args()
        return {"msg", "get"}

    def post(self):
        args = parse.parse_args()
        return {"msg", "post"}




# from flask import Blueprint, jsonify
# from flask_jwt_extended import jwt_required, get_jwt_identity
#
# from apps.models.user import MyUser
#
# reqt_bp = Blueprint("req", __name__, url_prefix="/reqt")
#
# @reqt_bp.route("/userinfo/")
# @jwt_required
# def get_user():
#     mu = MyUser()
#     current_user = get_jwt_identity()
#     return jsonify(logged_in_as=current_user), 200
#
