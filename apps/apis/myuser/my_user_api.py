from flask import g, current_app, session
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_restful import Resource, reqparse, abort, fields, marshal

from apps.apis.api_constant import HTTP_OK, HTTP_CREATE_OK, USER_ACTION_LOGIN, USER_ACTION_REGISTER
from apps.apis.myuser.model_utils import get_user
from apps.models.user.myuser import MyUser

"""
u'json': u'the JSON body',
    u'form': u'the post body',
    u'args': u'the query string',
    u'values': u'the post body or the query string',
    u'headers': u'the HTTP headers',
    u'cookies': u'the request\'s cookies',
    u'files': u'an uploaded file',
# 添加验证参数
        # 第一个参数： 传递的参数的名称
        # 第二个参数（location）： 传递参数的方式 args form  
        # 第三个参数（type）： 验证参数的函数(可以自定义验证函数)
        parser.add_argument('username', location='args', type=str)
        from flask_restful reqpes import RequestParser
好处： 过滤和转换类型
步骤：
1创建对象：
reqser = ReqserParser()
2添加参数声明：
reqser.add_argument(‘name’)
required 是否必须存在 True 必须 False 默认
help 错误时返回错误信息
type 参数类型 系统类型： int float , inputs type=inputs.int_range(1,100)
自定义类型 写一个自定义的函数
def mbile(phone) phone 被检测的手机号
if re.macth(‘r’1[3-9]\d{9}’,phone):
return phone
else:
raise ValireError().format()

location 指定从哪里获取参数
locaton=‘args’/'forme
action:是否保留第一个参数action=‘append’
3执行，返回参数对象
req = .parse_args()
4使用
name=req.name
"""
parse = reqparse.RequestParser()
parse.add_argument("username", type=str, required=True, help="请输入用户名!")
parse.add_argument("password", type=str, required=True, help="请输入密码!")
parse.add_argument("phone", type=str, required=True, help="请输入手机号!")
# 添加注册功能和登录 action
parse.add_argument("action", type=str, required=True, help="请确认请求参数!")

# sys_user 序列化模板
# 所有用户对象的模板
sys_users_fields = {
    "username": fields.String,
    "password": fields.String(attribute="_password"),  # 这是测试, 正常不返回
    "phone": fields.String
}
# 展示对象模板
single_user_field = {
    "status": fields.Integer,
    "msg": fields.String,
    "data": fields.Nested(sys_users_fields)
}


class My_User_Resource(Resource):

    def get(self):
        return {'msg': "ok"}

    def post(self):
        # 注册
        args = parse.parse_args()
        username = args.get("username")
        password = args.get("password")
        phone = args.get("phone")
        # action参数获取
        action = args.get("action").strip().lower()

        # 判断登录或注册
        if action == USER_ACTION_REGISTER:

            my_user = MyUser()
            my_user.username = username
            my_user.password = password
            my_user.phone = phone
            create_status = my_user.save()
            # print("-------------:", current_app.config["DEBUG"])  # 获取当前配置
            # 带错误提示
            if not create_status[0]:
                abort(400, msg="create fail: %s " % create_status[1] if current_app.config["DEBUG"] else "")

            data = {
                "status": HTTP_CREATE_OK,
                "msg": "用户创建成功",
                "data": my_user
            }

            # 先不用@marshal_with 装饰器
            return marshal(data=data, fields=single_user_field)
        # 登录
        elif action == USER_ACTION_LOGIN:
            user: MyUser = get_user(username) or get_user(phone)
            if not user:
                abort(400, msg="用户不存在!")
            if not user.check_password(password_val=password):
                abort(400, msg="密码错误!")
            # 生成token
            access_token = create_access_token(identity=user.id)
            refresh_token = create_refresh_token(identity=user.id)
            session["access_token"] = access_token
            data = {
                "msg": "loginSuccess",
                "status": HTTP_OK,
                "token": access_token
            }
            return data

        else:
            abort(400, msg={"登录或注册失败! 请提供正确参数!"})
