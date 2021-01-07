
def get_db_info(dbinfo:dict):
    engine = dbinfo.get("ENGINE") or "mysql"
    driver = dbinfo.get("DRIVER") or "pymysql"
    user = dbinfo.get("USER") or ""
    password = dbinfo.get("PASSWORD") or ""
    host = dbinfo.get("HOST") or "localhost"
    port = dbinfo.get("PORT") or "3306"
    dbname = dbinfo.get("DBNAME") or ""
    charset = dbinfo.get("CHARSET")
    return "{}+{}://{}:{}@{}:{}/{}?charset={}".format(engine, driver, user, password, host, port, dbname, charset)

class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = "sdfsdfsdf"
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost:3306/mydb"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # flask-session 配置
    SESSION_TYPE = "redis"
    SESSION_USE_SINER = True  # 对cookie中session_id进行隐藏处理 加密混淆
    PERMANENT_SESSION_LIFETIME = 20  # session数据的有效期, 单位秒

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
    SESSION_REDIS = ""


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
    'develop' : DevelopmentConfig,
    'product' : ProductionConfig
}