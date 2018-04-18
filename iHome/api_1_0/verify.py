#coding:utf-8

from flask import make_response,request,abort,jsonify

from iHome import redis_store
from iHome.utils.captcha.captcha import captcha
from iHome.utils.response_code import RET
from . import api


@api.route('/image_code',methods=["GET"])
def get_image_code():
    """提供图片验证码
    1.获取uuid，并校验uuid
    2.生成图片验证码
    3.使用redis数据库缓存图片验证码，uuid作为key
    4.响应图片验证码
    """

    # 1.获取uuid，并校验uuid

    uuid = request.args.get('uuid')

    if not uuid:
        abort(403)

    #2.⽣成图⽚验证码的名字，⽂本信息，图⽚
    name,text,image = captcha.generate_captcha()

    # 3.使用redis数据库缓存图片验证码，uuid作为key
    try:
        redis_store.set('ImageCode:%s' %uuid,text)
    except Exception as e:
        return jsonify(errno=RET.DBERR,errmsg=u'保存验证码失败')

    # 4.响应图片验证码
    response = make_response(image)
    # 设置响应头中的⽂件类型,指定响应的内容是image/jpg
    response.headers['Content-Type'] ='image/jpg'
    return response