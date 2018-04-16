#coding:utf-8

from flask import Flask
from  flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

class Config(object):

    DEBUG = True

app.config.from_object(Config)

# mysql连接配置
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@127.0.0.1:3306/iHome'
# mysql禁⽌追踪数据库增删改
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



@app.route('/')
def index():
    return "index"

if __name__ == "__main__":
    app.run()

