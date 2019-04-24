from app.base_class import FormBase
import hashlib
import re
import uuid
import datetime
from app import db
from app.model import TestUser, User

from app.setting import EMAIL_REX, PHONE_REX

class UserForm():

    form_data = ''

    def __init__(self, form_data_dict):
        if form_data_dict['method'] == 'register':
            self.register_form(form_data_dict['form'])

    def set_data(self, form_data):
        self.form_data = form_data

    def get_data(self):
        return self.form_data

    def register_form(self, form_data_dict):
        inter_num = 0
        status = ''
        message_list = []
        for key,val in form_data_dict.items():
            if key not in form_data_dict:
                message_list.append('缺少以下key：{0}'.format(key))
            if key == 'password':
                if len(val) >= 16 or len(val) <= 6:
                    message_list.append('密码长度需要在6到16位之间')
                    status = 'error'
                h1 = hashlib.md5(val.encode("utf8"))
                pwd = h1.hexdigest()
                form_data_dict['password'] = str(pwd)
            if key == 'name':
                user = db.session.query(User).filter(User.name == val).all()
                if user:
                    message_list.append('用户已存在')
                    status = 'error'
                if len(val) > 20:
                    message_list.append('用户名超出最大长度')
                    status = 'error'
            if key == 'email':
                email_rex_flag = re.match(EMAIL_REX, val)
                if not email_rex_flag:
                    message_list.append('邮箱地址不正确')
                    status = 'error'
            if key == 'phone':
                user = db.session.query(User).filter(User.phone == val).all()
                if user:
                    message_list.append('手机号码已存在')
                    status = 'error'
                phone_rex_flag = re.match(PHONE_REX, val)
                if not phone_rex_flag:
                    message_list.append('手机号码不正确')
                    status = 'error'
            if key == 'gender':
                if val not in ('0', '1'):
                    message_list.append('性别错误')
                    status = 'error'
                else:
                    form_data_dict['gender'] = int(val)
            inter_num += 1
        if inter_num != 5:
            message_list.append('传入参数数量错误')
            status = 'error'
        user_uuid = uuid.uuid1()
        form_data_dict['uuid'] = str(user_uuid)
        if not status:
            status = 'success'
        self.form_data = {'status': status, 'message': message_list, 'form': form_data_dict}