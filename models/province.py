from db import db


class Province(db.Model):
    __tablename__ = "provinces"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 主键，自增
    name = db.Column(db.String(48), unique=True)
    nowCon = db.Column(db.Integer)
    con = db.Column(db.Integer)
    heal = db.Column(db.Integer)
    dead = db.Column(db.Integer)
    citys = db.relationship("City", backref='province')
