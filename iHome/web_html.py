#coding:utf-8

from flask import Blueprint,current_app

html_blue = Blueprint('html',__name__)

@html_blue.route('/<re(r".*"):file_name>')
def get_static_html(file_name):


    if not file_name:
        file_name = 'index.html'

    if file_name != 'favicon.ico':
        file_name = 'html/%s'%file_name

    return current_app.send_static_file(file_name)
    # return render_template(file_name)
