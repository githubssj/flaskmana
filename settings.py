
# 获得SQLALCHEMY_DATABASE_URI的字符串
import redis


def get_db_info(dbinfo: dict):
    engine = dbinfo.get("ENGINE") or "mysql"
    driver = dbinfo.get("DRIVER") or "pymysql"
    user = dbinfo.get("USER") or ""
    password = dbinfo.get("PASSWORD") or ""
    host = dbinfo.get("HOST") or "localhost"
    port = dbinfo.get("PORT") or "3306"
    dbname = dbinfo.get("DBNAME") or ""
    charset = dbinfo.get("CHARSET")
    return "{}+{}://{}:{}@{}:{}/{}?charset={}".format(engine, driver, user, password, host, port, dbname, charset)


# 基本配置
class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = "sdfsdfsdf"   # cookie和session会用到
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost:3306/mydb"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # flask-session 配置
    # 把session保存到redis中
    # session存储方式为redis
    SESSION_TYPE = "redis"
    PERMANENT_SESSION_LIFETIME = 3600  # session数据的有效期, 单位秒
    # 设置session的默认存储名字, 存储的session的name就从session-> 变为ssj
    SESSION_COOKIE_NAME = "ssj"
    # 如果设置session的生命周期是否是会话期, 为True，则关闭浏览器session就失效
    # SESSION_PERMANENT = False
    # 是否对发送到浏览器上session的cookie值进行加密
    SESSION_USE_SIGNER = True
    # 保存到redis的session数的名称前缀
    SESSION_KEY_PREFIX = "flasksession:"
    # session保存数据到redis时启用的链接对象
    # SESSION_REDIS = redis.Redis(host='127.0.0.1', port='6379')  # 用于连接redis的配置


# 开发环境
class DevelopmentConfig(Config):
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "root",
        "HOST": "localhost",
        "PORT": "3306",
        "DBNAME": "mydb",
        "CHARSET": "utf8mb4"
    }
    DEBUG = True
    ENV = 'development'
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost:3306/mydb?charset=utf8mb4'"
    SQLALCHEMY_DATABASE_URI = get_db_info(dbinfo=dbinfo)
    """
    如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。
    """
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SESSION_REDIS = redis.Redis(host='127.0.0.1', port='6379')


# 生产环境
class ProductionConfig(Config):
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost:3306/mydb?charset=utf8mb4'"
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "root",
        "HOST": "localhost",
        "PORT": "3306",
        "DBNAME": "mydb",
        "CHARSET": "utf8mb4"
    }
    SQLALCHEMY_DATABASE_URI = get_db_info(dbinfo=dbinfo)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_REDIS = ""


# 测试环境
class TestingConfig(Config):
    TESTING = True


# 参数字典
config_map = {
    'develop': DevelopmentConfig,
    'product': ProductionConfig
}
