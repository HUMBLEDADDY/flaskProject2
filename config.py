# -*- coding: utf-8 -*-
#配置类
class Config(object):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://debian-sys-maint:5Dvjr3MiDzszFpY3@127.0.0.1:3306/epidemic"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True  # 会打印原生sql语句，便于观察测试
    SECRET_KEY="root"

SECRET_KEY = 'abcdefghijklmm'