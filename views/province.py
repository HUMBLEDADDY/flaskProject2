# -*- coding: utf-8 -*-
from flask import Blueprint,render_template,request,jsonify
from models.province import Province
from checkToken import verify_auth_token

province=Blueprint('province',__name__,template_folder='../templates/province')

#获取所有的省份疫情信息
@province.route('/all', methods=['GET'])
def all():
    #token校验
    try:
        token = request.headers["token"]
    except Exception as e:
        return {'tips': '请先登录'}, 401
    if verify_auth_token(token):
        try:
            provinces=Province.query.all()
            datas = []
            for i in provinces:
                nprovince = {}
                nprovince['id'] = i.id
                nprovince['name'] = i.name
                nprovince['nowCon'] = i.nowCon
                nprovince['con'] = i.con
                nprovince['heal'] = i.heal
                nprovince['dead'] = i.dead
                datas.append(nprovince)
            return jsonify(datas), 200
        except Exception as e:
            return {'tips': '抱歉后台出了一点小错误'}, 205
    else:
        return {'tips': '请先登录'}, 401



