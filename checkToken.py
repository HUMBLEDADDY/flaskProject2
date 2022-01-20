
'''
checkToken.py
用于校验token
具体token的生成由User类提供的方法
'''

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer #用于生成token
from itsdangerous import BadSignature, SignatureExpired #用于生成token
from flask_httpauth import HTTPBasicAuth #用于生成token
from config import SECRET_KEY #获取密码

auth = HTTPBasicAuth() #定义认证对象

def verify_auth_token(token):
    s = Serializer(SECRET_KEY)
    # token正确
    try:
        data = s.loads(token)
        return data
    # token过期
    except SignatureExpired:
        return False
    # token错误
    except BadSignature:
        return False
