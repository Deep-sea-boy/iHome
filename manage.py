#coding:utf-8

from flask import Flask
from  flask_sqlalchemy import SQLAlchemy
import redis
from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand

app = Flask(__name__)

class Config(object):

    DEBUG = True
    REDIS_HOST = '127.0.0.1'
    REDIE_PORT = 6379

app.config.from_object(Config)

# mysql连接配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@127.0.0.1:3306/iHome'
# mysql禁⽌追踪数据库增删改
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# 在迁移时让app和db建⽴关联
Migrate(app,db)

redis_store = redis.StrictRedis(host=Config.REDIS_HOST,port=Config.REDIE_PORT)

manager = Manager(app)
# 将迁移脚本添加到脚本管理器
manager.add_command('db',MigrateCommand)

@app.route('/')
def index():

    redis_store.set('name','zhs')
    return "index"

if __name__ == "__main__":
    manager.run()

