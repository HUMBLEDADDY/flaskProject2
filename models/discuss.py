# -*- coding: utf-8 -*-
from ..db import db


class Discuss(db.Model):
    __tablename__ = "discusses"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.Text)
    time = db.Column(db.String(100))
    share_id = db.Column(db.Integer, db.ForeignKey("shares.id"))
    uid = db.Column(db.Integer, db.ForeignKey("users.id"))
