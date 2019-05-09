from flask import render_template, Blueprint, redirect, url_for
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
        register_return= UserAPI().register()
        if register_return['status'] != 'success':
            flash('注册失败{0}'.format(register_return['message']), 'error')
        else:
            flash('注册成功', 'success')
        return redirect(url_for('index'))
    else:
        print('无效的方式')


@user.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        login_return = UserAPI().login()
        if login_return['status'] != 'success':
            flash('登陆失败{0}'.format(login_return['message']), 'error')
        else:
            flash('登陆成功', 'success')
        return render_template('index.html')

@user.route('/login_page/', methods=['POST', 'GET'])
def login_page():
    if request.method == 'GET':
        return render_template('user/user_login.html')
