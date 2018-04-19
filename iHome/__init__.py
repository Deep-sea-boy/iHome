#coding:utf-8
import logging
from logging.handlers import RotatingFileHandler

import redis
from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

from config import configs
from iHome.utils.commom import RegexConverter

def setUpLogging(level):
    # 设置⽇志的记录等级
    logging.basicConfig(level=level) # 调试debug级
    # 创建⽇志记录器，指明⽇志保存的路径、每个⽇志⽂件的最⼤⼤⼩、保存的⽇志⽂件个数上限
    file_log_handler = RotatingFileHandler("logs/logs", maxBytes=1024*1024*100, backupCount=10)
    # 创建⽇志记录的格式 ⽇志等级 输⼊⽇志信息的⽂件名 ⾏数 ⽇志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的⽇志记录器设置⽇志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的⽇志⼯具对象（flask app使⽤的）添加⽇志记录器
    logging.getLogger().addHandler(file_log_handler)


db = SQLAlchemy()
redis_store = None

def get_app(config_name):

    setUpLogging(configs[config_name].LOGGING_LEVEL)
    app = Flask(__name__)

    app.config.from_object(configs[config_name])

    db.init_app(app)

    global redis_store
    redis_store = redis.StrictRedis(host=configs[config_name].REDIS_HOST,port=configs[config_name].REDIS_PORT)

    # 开启CSRF保护:flask需要自己讲csrf_token写入到浏览器的cookie
    CSRFProtect(app)

    # 使⽤flask_session扩展存储session到Redis数据库
    Session(app)

    #注意点：需要先有正则转换器，才能匹配路由
    #讲自定义路由转换器添加到转换器列表
    app.url_map.converters['re']= RegexConverter

    from iHome.api_1_0 import api
    app.register_blueprint(api)

    from web_html import html_blue
    app.register_blueprint(html_blue)



    return app