
#配置类
class Config(object):
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:0101czx724715@127.0.0.1:3306/epidemic"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:0101czx7215@127.0.0.1:3306/epidemic?charset=utf8mb4"
    SQLALCHEMY_CHARSET = 'utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_ECHO = True  # 会打印原生sql语句，便于观察测试
    SECRET_KEY="root"

SECRET_KEY = 'abcdefghijklmm'