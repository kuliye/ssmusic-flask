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
        register_return= user.post()
        if register_return['status'] != 'success':
            flash('注册失败{0}'.format(register_return['message']), 'error')
        else:
            flash('注册成功', 'success')
        return render_template('index.html')
    else:
        print('sasas')