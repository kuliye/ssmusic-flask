from flask import session
from flask.views import View, MethodView
from app.Base import Appliction

class IndexAPI(MethodView):

    user = ''

    def __init__(self):
        self.user = session.get('user')
    def index(self):
        self.user = session.get('user')
