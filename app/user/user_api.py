from datetime import datetime

from flask import render_template, Blueprint
from flask.views import View, MethodView

from .user_form import UserForm
from app.model import TestUser
from app import db


class UserAPI(MethodView):

    def get(self, user_id):
        if user_id is None:
            return render_template('user/user_register.html')
        else:
            return 'user'

    def post(self):
        user = UserForm()
        form_data = user.register_form()
        user = TestUser(form_data['name'], form_data['password'], datetime.now())
        db.session.add(user)
        db.session.commit()
        print(form_data)
        return 0

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
