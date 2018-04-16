#coding:utf-8

import redis
from flask import Flask,session
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)



class Config(object):

    DEBUG = True
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    # mysql连接配置
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/iHome'
    # mysql禁⽌追踪数据库增删改
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 秘钥
    SECRET_KEY = 'q7pBNcWPgmF6BqB6b5VICF7z7pI+90o0O4CaJsFGjzRsYiya9SEgUDytXvzFsIaR'

    # 配置session参数
    # 指定session存储到redis
    SESSION_TYPE = 'redis'
    # 指定要使用的redis的位置
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # 是否使用secret_key签名session_data
    SESSION_USE_SIGNER = True
    # 设置session的过期时间
    PERMANENT_SESSION_LIFETIME = 3600 * 24  # 有效期为一天


app.config.from_object(Config)

db = SQLAlchemy(app)

# 在迁移时让app和db建⽴关联
Migrate(app,db)

redis_store = redis.StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_PORT)

# 开启CSRF保护:flask需要自己讲csrf_token写入到浏览器的cookie
CSRFProtect(app)

# 使⽤flask_session扩展存储session到Redis数据库
Session(app)

manager = Manager(app)
# 将迁移脚本添加到脚本管理器
manager.add_command('db',MigrateCommand)

@app.route('/',methods=['GET','POST'])
def index():

    redis_store.set('name','zhs')
    session['age'] =22
    return "index"

if __name__ == "__main__":
    manager.run()

