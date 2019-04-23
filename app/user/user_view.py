from flask import render_template, Blueprint
from flask.views import View, MethodView
from flask import request, flash

from flask.views import View
from . import user
from .user_api import UserAPI


@user.route('/register/', methods=['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('user/user_register.html')
    elif request.method == 'POST':
        user = UserAPI()
        status = user.post()
        echo = '0'
        if echo == '0':
            flash('数据库操作失败', 'error')
        else:
            pass
        return render_template('index.html', context={'status': status})
    else:
        print('sasas')