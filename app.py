
from flask import Flask, request
from config import Config


# from . import views
from views.city import city
from views.discuss import discuss
from views.province import province
from views.share import share
from views.user import user

from db import db
from flask_cors import CORS


app = Flask(__name__)

CORS(app, supports_credentials=True) #解决跨域问题

app.config.from_object(Config) #设置Config

app.register_blueprint(user,url_prefix='/user')
app.register_blueprint(province,url_prefix='/province')
app.register_blueprint(city,url_prefix='/city')
app.register_blueprint(share,url_prefix='/share')
app.register_blueprint(discuss,url_prefix='/discuss')

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

with app.app_context():
    db.init_app(app)
    db.create_all()


if __name__ == '__main__':
    db.init_app(app)
    app.app_context().push()

    #更新疫情数据，在这里import是因为更新数据需要数据库的连接，所以要在db.init_app(app)之后
    from createtable import initData
    initData()
    app.run(host="0.0.0.0",port = 5000)
