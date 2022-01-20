# -*- coding: utf-8 -*-
from db import db


class Share(db.Model):
    __tablename__ = "shares"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.Text)
    time = db.Column(db.String(100))
    title = db.Column(db.String(100))
    uid = db.Column(db.Integer, db.ForeignKey("users.id"))
    discusses = db.relationship("Discuss", backref="share")
