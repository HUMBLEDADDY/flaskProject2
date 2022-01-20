from flask import Blueprint,render_template, jsonify,request
from models.share import Share
from checkToken import verify_auth_token
import datetime
import time
from db import db

share=Blueprint('share',__name__,template_folder='../templates/share')

#获取所有的分享
@share.route('/list', methods=['GET'])
def list():
    #token校验
    try:
        token = request.headers["token"]
    except Exception as e:
        return {'tips': '请先登录'}, 401
    if verify_auth_token(token):
        try:
            shares = Share.query.all()
            datas = []
            for i in shares:
                nshare = {}
                nshare['id'] = i.id
                nshare['title'] = i.title
                nshare['text'] = i.text
                nshare['time'] = i.time
                nshare['uid'] = i.uid
                datas.append(nshare)
            return jsonify(datas), 200

        except Exception as e:
            return {'tips': '抱歉后台出了一点小错误'}, 205
    else:
        return {'tips': '请先登录'}, 401

#信件一篇分享
@share.route('/create', methods=['POST'])
def create():
    #token校验
    try:
        token = request.headers["token"]
    except Exception as e:
        return {'tips': '请先登录'}, 401
    if verify_auth_token(token):
        share = request.json.get('share')
        title = share['title']
        text = share['blogContent']
        uid = verify_auth_token(token)['id'] #从token中解析用户id
        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S');#格式化当前时间
        share = Share(title = title,text = text,uid = uid,time = time)
        try:
            db.session.add(share)
            db.session.commit()
            return {'tips': '添加成功！'}, 200

        except Exception as e:
            return {'tips': '抱歉后台出了一点小错误'}, 201
    else:
        return {'tips': '请先登录'}, 401

#获取某一篇分享的详细信息
@share.route('/content', methods=['GET'])
def content():
    #token校验
    try:
        token = request.headers["token"]
    except Exception as e:
        return {'tips': '请先登录'}, 401
    if verify_auth_token(token):
        id = request.args.get('id')
        try:
            i = Share.query.filter(Share.id == id).first()
            nshare = {}
            nshare['id'] = i.id
            nshare['title'] = i.title
            nshare['text'] = i.text
            nshare['time'] = i.time
            nshare['uid'] = i.uid
            return jsonify(nshare), 200

        except Exception as e:
            return {'tips': '抱歉后台出了一点小错误'}, 201

    else:
        return {'tips': '请先登录嗷！'}, 401

@share.route('/getMyshare', methods=['GET'])
def getMyshare():
    try:
        token = request.headers["token"]
    except Exception as e:
        return {'tips': '请先登录'}, 401
    if verify_auth_token(token):
        # try:
        uid = verify_auth_token(token)['id'] #从token中解析用户id
        shares = Share.query.filter(Share.uid == uid).all()
        datas = []
        for i in shares:
            nshare = {}
            nshare['id'] = i.id
            nshare['title'] = i.title
            nshare['text'] = i.text
            nshare['time'] = i.time
            nshare['uid'] = i.uid
            datas.append(nshare)
        return jsonify(datas), 200

        # except Exception as e:
        #     return {'tips': '抱歉后台出了一点小错误'}, 205
    else:
        return {'tips': '请先登录'}, 401