from app.base_class import FormBase
import hashlib
import re
import uuid
import datetime
from app import db
from app.model import TestUser, User

from app.setting import EMAIL_REX, PHONE_REX
from flask import session

class UserForm():

    form = ''

    def __init__(self, form_data_dict):
        if form_data_dict['method'] == 'register':
            self.register_form(form_data_dict['form'])
        if form_data_dict['method'] == 'login':
            self.login_form(form_data_dict['form'])

    def set_form(self, form):
        self.form = form

    def get_form(self):
        return self.form

    def register_form(self, form_data_dict):
        status = 'success'
        message_list = {}
        key_list = ['password', 'name', 'phone', 'email', 'gender']
        if sorted([key for key, value in form_data_dict.items()]) != sorted(key_list):
            message_list['key_error'] = 'key错误'
        else:
            if len(form_data_dict['password']) >= 16 or len(form_data_dict['password']) <= 6:
                message_list['password_error'] = '密码长度需要在6到16位之间'
            else:
                h1 = hashlib.md5(form_data_dict['password'].encode("utf8"))
                pwd = h1.hexdigest()
                form_data_dict['password'] = str(pwd)

            user = db.session.query(User).filter(User.name == form_data_dict['name']).all()
            if user:
                message_list['name_error'] = '用户已存在'
            elif len(form_data_dict['name']) > 20:
                message_list['name_error'] = '用户名超出最大长度'

            email_rex_flag = re.match(EMAIL_REX, form_data_dict['email'])
            if not email_rex_flag:
                message_list['email_error'] = '邮箱地址不正确'

            user = db.session.query(User).filter(User.phone == form_data_dict['phone']).all()
            phone_rex_flag = re.match(PHONE_REX, form_data_dict['phone'])
            if user:
                message_list['phone_error'] = '手机号码已存在'
            elif not phone_rex_flag:
                message_list['phone_error'] = '手机号码不正确'

            if form_data_dict['gender'] not in ('0', '1'):
                message_list['gender_error'] = '性别错误'
            else:
                form_data_dict['gender'] = int(form_data_dict['gender'])

            user_uuid = uuid.uuid1()
            form_data_dict['uuid'] = str(user_uuid)
            if not message_list == {}:
                status = 'error'
        self.form = {'status': status, 'message': message_list, 'form': form_data_dict}


    def login_form(self, form_data_dict):
        status = 'success'
        message_list = {}
        key_list = ['password', 'name']
        if sorted([key for key, value in form_data_dict.items()]) != sorted(key_list):
            message_list['key_error'] = 'key错误'
        name = form_data_dict['name']
        password = form_data_dict['password']
        if name:
            user = db.session.query(User).filter(User.name == name).first()
            h1 = hashlib.md5(password.encode("utf8"))
            pwd = str(h1.hexdigest())
            auth_flag = user.pwd == pwd
            if auth_flag:
                session['user'] = {
                    'name': user.name,
                    'gender': user.gender,
                    'phone': user.phone,
                    'email': user.email,
                    'uuid': user.uuid
                }
            else:
                message_list['auth_error'] = '密码错误'
        else:
            message_list['user_error'] = '用户不存在'
        if not message_list == {}:
            status = 'error'

        self.form = {'status': status, 'message': message_list}

