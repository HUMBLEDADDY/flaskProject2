# -*- coding: utf-8 -*-
'''
createtable.py用于从接口获取数据并将其存放至数据库
'''

import time
import json
import requests
from app import app
from db import db
from models.city import City
from models.province import Province

#用pymysql实现省表和市表的截断
import pymysql
pydb = pymysql.connect(host="localhost", user="debian-sys-maint", passwd="5Dvjr3MiDzszFpY3", db = "epidemic", charset='utf8')

def initData():
    cursor = pydb.cursor()

    #截断市表（全部删除）
    sql = "TRUNCATE TABLE citys"
    try:
        result = cursor.execute(sql)
        print(result)
        pydb.commit()
        print('删除成功')
    except Exception as e:
        print(e)
        pydb.rollback()

    #取消外键的约束
    sql = "SET foreign_key_checks = 0"
    try:
        result = cursor.execute(sql)
        pydb.commit()
    except Exception as e:
        print(e)
        pydb.rollback()

    #截断省表（全部删除）
    sql = "TRUNCATE TABLE provinces"
    try:
        result = cursor.execute(sql)
        pydb.commit()
        print('删除成功')
    except Exception as e:
        print(e)
        pydb.rollback()

    #恢复外键的约束
    sql = "SET foreign_key_checks = 1"
    try:
        result = cursor.execute(sql)
        pydb.commit()
    except Exception as e:
        print(e)
        pydb.rollback()

    #获取json
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%d' % int(time.time() * 1000)
    html = requests.get(url)

    #开始解析json,获取疫情数据
    data = json.loads(html.json()['data'])
    china_data = data['areaTree'][0]['children']
    for cd in china_data:
        name = cd['name']
        nowCon = cd['total']['nowConfirm']
        con = cd['total']['confirm']
        heal = cd['total']['heal']
        dead = cd['total']['dead']
        if int(nowCon)<0:
            nowCon=int(con)-int(heal)
        if nowCon>=0:
            province = Province(name=name, nowCon=nowCon, con=con, heal=heal, dead=dead)
        city_data = cd['children']
        for j in city_data:
            name = j['name']
            nowCon = j['total']['nowConfirm']
            con = j['total']['confirm']
            heal = j['total']['heal']
            dead = j['total']['dead']
            if nowCon < 0:
                con = abs(nowCon)
                nowCon = con - heal-dead
            if nowCon>=0:
                 city = City(name=name, nowCon=nowCon, con=con, heal=heal, dead=dead)
                 province.citys.append(city)
            #print(citys)
        try:
            db.session.add(province)
            db.session.commit()
        except Exception as e:
            print(e)
            pydb.rollback()







