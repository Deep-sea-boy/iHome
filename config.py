#coding:utf-8
import logging

import redis


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

class Development(Config):
    LOGGING_LEVEL = logging.DEBUG

class Production(Config):
    LOGGING_LEVEL = logging.WARN
    DEBUG = False
    # mysql连接配置
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/iHome_GZ'


class Unitest(Config):
    TESTING = True
    # 设置session的过期时间
    PERMANENT_SESSION_LIFETIME = 3600 * 24 *2 # 有效期为一天
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/iHome_Unitest'

configs = {
    'dev':Development,
    'pro':Production,
    'uni':Unitest
}