
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
    DEBUG = True
    ENV = 'development'
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost:3306/mydb"
    """
    如果设置成 True (默认情况)，Flask-SQLAlchemy 将会追踪对象的修改并且发送信号。这需要额外的内存， 如果不必要的可以禁用它。
    """
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SESSION_REDIS = ""


# 生产环境
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost:3306/mydb"
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