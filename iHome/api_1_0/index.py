#coding:utf-8

from iHome import redis_store
from . import api


@api.route('/',methods=["GET","POST"])
def index():
    redis_store.set('name','zhs')
    return 'index success'