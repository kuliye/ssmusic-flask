from app import app
from flask import render_template, Blueprint
from flask.views import View, MethodView
from flask import request

from . import user

# @user.route("/")
# def user_login():
#     return render_template("index.html")



class UserForm():
    def register_form(self):
        data = request.get_json()
        return data

class UserAPI(MethodView):

    def get(self, user_id):
        '''
        用户登陆
        :param user_id:
        :return:
        '''
        if user_id is None:
            # return a list of users
            return render_template('user/user_register.html')
        else:
            # expose a single user
            return 'user'

    def post(self):
        name = request.form.get('name', '')
        password = request.form.get('passwod', '')
        content = {"name": name, "password": password}
        data = request.form
        return str(data)

    def delete(self, user_id):
        # delete a single user
        pass

    def put(self, user_id):
        # update a single user
        pass


user_view = UserAPI.as_view('user_api')
user.add_url_rule('/', defaults={'user_id': None},
                 view_func=user_view, methods=['GET',])
user.add_url_rule('/', view_func=user_view, methods=['POST',])
user.add_url_rule('/<int:user_id>', view_func=user_view,
                 methods=['GET', 'PUT', 'DELETE'])


#
# def register_api(view, endpoint, url, pk='id', pk_type='int'):
#     view_func = view.as_view(endpoint)
#     user.add_url_rule(url, defaults={pk: None},
#                      view_func=view_func, methods=['GET',])
#     user.add_url_rule(url, view_func=view_func, methods=['POST',])
#     user.add_url_rule('%s<%s:%s>' % (url, pk_type, pk), view_func=view_func,
#                      methods=['GET', 'PUT', 'DELETE'])
#
# register_api(UserAPI, 'user_api', '/', pk='user_id')