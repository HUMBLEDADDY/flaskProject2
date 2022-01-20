# -*- coding: utf-8 -*-
from flask import Blueprint,render_template,request,jsonify
from models.city import City
from checkToken import verify_auth_token

city=Blueprint('city',__name__,template_folder='../templates/city')

#获取所有的城市疫情信息
@city.route('/all', methods=['GET'])
def all():
    #token校验
    try:
        token = request.headers["token"]
    except Exception as e:
        return {'tips': '请先登录'}, 401
    if verify_auth_token(token):
        try:
            citys=City.query.all()
            datas = []
            for i in citys:
                ncity = {}
                ncity['id'] = i.id
                ncity['name'] = i.name
                ncity['nowCon'] = i.nowCon
                ncity['con'] = i.con
                ncity['heal'] = i.heal
                ncity['dead'] = i.dead
                ncity['prov_id'] = i.prov_id
                datas.append(ncity)
            return  jsonify(datas),200
        except Exception as e:
            print(e)
            return {'tips': '抱歉后台出了一点小错误'}, 205
    else:
        return {'tips': '请先登录'}, 401

