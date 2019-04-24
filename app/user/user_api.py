from datetime import datetime

from flask import render_template, Blueprint, request
from flask.views import View, MethodView

from .user_form import UserForm
from app.model import TestUser, User
from app import db


class UserAPI(MethodView):

    def get(self, user_id):
        if user_id is None:
            return render_template('user/user_register.html')
        else:
            return 'user'

    def post(self):
        form_data = request.form
        form_data_dict = dict(form_data)
        user_form = {'method': 'register', 'form':form_data_dict }
        data = UserForm(user_form).get_data()
        if data['status'] == 'success':
            user = User(data['form'])
            db.session.add(user)
            db.session.commit()
            status = 'success'
        else:
            status = 'error'
        return {'status': status, 'message': data['message']}

    def delete(self, user_id):
        pass


# def register_api(view, endpoint, url, pk='id', pk_type='int'):
#     view_func = view.as_view(endpoint)
#     user.add_url_rule(url, defaults={pk: None},
#                      view_func=view_func, methods=['GET',])
#     user.add_url_rule(url, view_func=view_func, methods=['POST',])
#     user.add_url_rule('%s<%s:%s>' % (url, pk_type, pk), view_func=view_func,
#                      methods=['GET', 'PUT', 'DELETE'])
# register_api(UserAPI, 'user_api', '/user_api/', pk='user_id')
