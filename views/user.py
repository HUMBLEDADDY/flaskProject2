# -*- coding: utf-8 -*-
from flask import Blueprint,render_template,request
from ..models.user import User
from ..db import db
from ..checkToken import verify_auth_token

user=Blueprint('user',__name__,template_folder='../templates/user')

#注册
@user.route('/register',methods=['POST'])
def register():
    user = request.json.get('user')
    password = request.json.get('password')
    newUser = User(name = user,password = password)
    # try:
    db.session.add(newUser)
    db.session.commit()
    return {'tips':'注册成功'},200

    # except Exception as e:
    #     return {'tips':'该用户名已被注册，换一个吧！'},201

#登录
@user.route('/login',methods=['POST'])
def login():
    print(request.json)
    user = request.json.get('user')
    password = request.json.get('password')
    newUser = User(name = user)

    # try:
    possibleUser = User.query.filter(User.name == user).first()
    token = possibleUser.generate_auth_token().decode('ascii')

    if possibleUser.password == password:
        return {'tips':'登录成功!','token':token},200
    else:
        return {'tips':'密码是不是输错了？小傻逼'},202
    #
    # except Exception as e:
    #     return {'tips':'用户名是不是输错了？大傻逼'},201
