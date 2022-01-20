from db import db
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from config import SECRET_KEY

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 主键，自增
    name = db.Column(db.String(48), unique=True)
    password=db.Column(db.String(48))
    discusses = db.relationship("Discuss", backref="user")
    shares = db.relationship("Share", backref="user")

    def generate_auth_token(self, expiration = 6000):
        s = Serializer(SECRET_KEY, expires_in = expiration)
        return s.dumps({ 'id': self.id })



