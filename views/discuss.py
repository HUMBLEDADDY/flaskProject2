
from models.discuss import Discuss
from flask import Blueprint,render_template,request,jsonify
from flask_httpauth import HTTPBasicAuth #用于生成token
from db import db
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer #用于生成token
from itsdangerous import BadSignature, SignatureExpired #用于生成token
from checkToken import verify_auth_token
import datetime
import time

discuss=Blueprint('discuss',__name__,template_folder='../templates/discuss')

#获取某一篇分享所有的评论
@discuss.route('/list', methods=['GET'])
def list():
    #token校验
    try:
        token = request.headers["token"]
    except Exception as e:
        return {'tips': '请先登录'}, 401
    if verify_auth_token(token):
        try:
            share_id = request.args.get('id')
            Discusses = Discuss.query.filter(Discuss.share_id == share_id).all()
            datas = []
            for i in Discusses:
                ndiscuss = {}
                ndiscuss['id'] = i.id
                ndiscuss['text'] = i.text
                ndiscuss['time'] = i.time
                ndiscuss['uid'] = i.uid
                ndiscuss['share_id'] = i.share_id
                datas.append(ndiscuss)
            return jsonify(datas), 200
        except Exception as e:
            return {'tips': '抱歉后台出了一点小错误'}, 205
    else:
        return {'tips': '请先登录'}, 401

#创建评论
@discuss.route('/create', methods=['post'])
def create():
    #token校验
    try:
        token = request.headers["token"]
    except Exception as e:
        return {'tips': '请先登录'}, 401
    if verify_auth_token(token):
        try:
            share_id = request.json.get('share_id')
            content = request.json.get('content')
            time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S');
            user_id = verify_auth_token(token)['id'] #从token中解析用户id
            newDiscusses = Discuss(share_id = share_id,uid = user_id,text = content,time = time)
            db.session.add(newDiscusses)
            db.session.commit()
            return {'tips': '创建成功'}, 200
        except Exception as e:
            return {'tips': '抱歉后台出了一点小错误'}, 205
    else:
        return {'tips': '请先登录'}, 401



