from app.base_class import FormBase
import hashlib
import re
import uuid
import datetime
from app import db
from app.model import TestUser, User

from app.setting import EMAIL_REX, PHONE_REX

class UserForm():

    form = ''

    def __init__(self, form_data_dict):
        if form_data_dict['method'] == 'register':
            self.register_form(form_data_dict['form'])

    def set_form(self, form):
        self.form = form

    def get_form(self):
        return self.form

    def register_form(self, form_data_dict):
        status = 'success'
        message_list = {}
        key_list = ['password', 'name', 'phone', 'email', 'gender']
        if sorted([key for key, value in form_data_dict.items()]) != sorted(key_list):
            status = 'error'
            message_list['key_error'] = 'key错误'
        else:
            for key,val in form_data_dict.items():
                if key == 'password':
                    if len(val) >= 16 or len(val) <= 6:
                        message_list['password_error'] = '密码长度需要在6到16位之间'
                    h1 = hashlib.md5(val.encode("utf8"))
                    pwd = h1.hexdigest()
                    form_data_dict['password'] = str(pwd)
                if key == 'name':
                    user = db.session.query(User).filter(User.name == val).all()
                    if user:
                        message_list['name_error'] = '用户已存在'
                    elif len(val) > 20:
                        message_list['name_error'] = '用户名超出最大长度'
                if key == 'email':
                    email_rex_flag = re.match(EMAIL_REX, val)
                    if not email_rex_flag:
                        message_list['email_error'] = '邮箱地址不正确'
                if key == 'phone':
                    user = db.session.query(User).filter(User.phone == val).all()
                    phone_rex_flag = re.match(PHONE_REX, val)
                    if user:
                        message_list['phone_error'] = '手机号码已存在'
                    elif not phone_rex_flag:
                        message_list['phone_error'] = '手机号码不正确'
                if key == 'gender':
                    if val not in ('0', '1'):
                        message_list['gender_error'] = '性别错误'
                    else:
                        form_data_dict['gender'] = int(val)
            user_uuid = uuid.uuid1()
            form_data_dict['uuid'] = str(user_uuid)
            if not message_list:
                status = 'error'
        self.form = {'status': status, 'message': message_list, 'form': form_data_dict}