# flaskmana

#migrate 步骤
1. python manage.py db init  # 第一次初始化时用  
2. 记得在写完model的class后, 导入在migrate的py文件中  
3. python manage.py db migrate  #每次修改后执行 再执行第4步  
4. -- 更新用 python manage.py db upgrade  

创建迁移仓库#  
这个命令会创建migrations文件夹，所有迁移文件都放在里面。  
python manage.py db init   # 将database.py替换为有manager.run()的执行文件  
创建迁移脚本#  
自动创建迁移脚本有两个函数  
upgrade()：函数把迁移中的改动应用到数据库中。  
downgrade()：函数则将改动删除。  
自动创建的迁移脚本会根据模型定义和数据库当前状态的差异，生成upgrade()和downgrade()函数的内容。  
对比不一定完全正确，有可能会遗漏一些细节，需要进行检查  
python manage.py db migrate -m 'initial migration'  # 第一次迁移不要使用 - m  
更新数据库#  
python manage.py db upgrade  
返回以前的版本#  
可以根据history命令找到版本号,然后传给downgrade命令:  
python manage.py db history  

输出格式：<base> ->  版本号 (head), initial migration  
回滚到指定版本  
python manage.py db downgrade 版本号  


# 安装 pip install flask-jwt-extended  
# 安装 pip install flask-restful  

pip install redis   

# 查看session时效: ttl  key    (秒)  
# url_for('static', filename="css/***.css")
# flask-debugtoolbar  pip install flask-debugtoolbar   
配合 templates的html使用  

# 创建model类  
class Animal:  
    __abstract__=True  # 这样继承的就不会与父类为一个表
class Dog(Animal):  
class Cat(Animal):    

# 数据库优化  
数据库连接池  
SQLALCHEMY_POOL_SIZE	数据库连接池的大小。默认是数据库引擎的默认值 （通常是 5）。  
SQLALCHEMY_POOL_TIMEOUT	指定数据库连接池的超时时间。默认是 10。  
SQLALCHEMY_POOL_RECYCLE	自动回收连接的秒数。这对 MySQL 是必须的，默认 情况下 MySQL 会自动移除闲置 8 小时或者以上的连接。 需要注意地是如果使用 MySQL 的话， Flask-SQLAlchemy 会自动地设置这个值为 2 小时。  
SQLALCHEMY_MAX_OVERFLOW	控制在连接池达到最大值后可以创建的连接数。当这些额外的 连接回收到连接池后将会被断开和抛弃。  
SQLALCHEMY_TRACK_MODIFICATIONS	如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。  

# return render_template("getcats.html", **locals())  # **local() 将所有参数传出  


# cache flask-cache(flask1.0以下可用)  
相同结果集查询从cache中取  
# flask-caching 1.0以上版本可用
    config = {
        "DEBUG": True,          # some Flask specific configs
        "CACHE_TYPE": "simple", # Flask-Caching related configs
        "CACHE_DEFAULT_TIMEOUT": 300
    }  
    cache = Cache(config={'CACHE_TYPE': 'simple'})  
    cache.init_app(app)  
    @cache.cached(timeout=50)  
    def index():  
        return render_template('index.html')  
        
# 钩子函数  
- 面向切面编程  
- 动态介入请求流程  
- before_request  
- after_request  
app 和 蓝图 都有  
       
# 4个内置对象
    request  
    session  
    g  
        跨函数传递数据  
        - 间接传递数据  
    config  
        使用config
        current_app.config 一定是在项目启动之后用  import flask.current_app  

# flask-restful  
/hello/的地址
post 请求 /hello 这时会报 301 问题  
解决:  restapi.add_resource(HelloResource, "/helloapi/", strict_slashes = False)  
在addresource 添加 strict_slashes = False  
  
# 输出   
- 输出默认字典: 可以直接进行序列化
- 输出包含对象:  
    -默认会抛出异常,对象不可json序列化  
    使用格式化工具: mashal 函数   
    mashal_with  装饰器  
    条件:  
        格式:
            字典格式,允许嵌套  
            value是fields.xxx fields.Nest  
            fields.List(fields.Nested(xx_fields))
        数据:  
            允许任何格式, 但是要根据模板定制  
        如果格式与数据完全对应,数据就是预格式  
        如果格式比数据字段多, 依然正常输出, 但是不存在的值为默认值 
        如果格式比数据字段少, 依然正常输出, 少的字段不显示  
    结论: 想要什么样的格式数据, 模板就是一样的格式, 与传入的数据关系不大  
  添加输出名: 与原数据库名不一致, 对外显示名 = fields.String(attribute="数据字段名")  
  这里的就是显示的名字 
          
# 数值交换
    python  
    1. a, b = b, a  
    2. temp =a a = b  b = temp  
    3. ^  异或 不同为1 相同为0  
         a = a^ b  
         b = a ^ b
         a = a ^ b  
    
    linux 权限
    十位 第一位类型 后9位每3位一组  
    用户  
    用户所在组  
    其他用户(组)   
    每一组  
    r  4 100  读权限  
    w  2 010  写权限  
    x  1 001  执行权限  
    例 5 : 101 
    权限匹配用 & 与   
    方便数据清洗: 按位与  
    同为1则1 其他为0    
    101 & 001 有执行权限   
        
         
        