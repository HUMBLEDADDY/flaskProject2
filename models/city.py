from db import db


class City(db.Model):
    __tablename__ = "citys"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 主键，自增
    name = db.Column(db.String(48))
    # 头像地址，文件夹名+文件名
    nowCon = db.Column(db.Integer)
    con = db.Column(db.Integer)
    heal = db.Column(db.Integer)
    dead = db.Column(db.Integer)
    prov_id = db.Column(db.Integer, db.ForeignKey('provinces.id'))
