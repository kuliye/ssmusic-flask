from flask import Blueprint

user = Blueprint("user", __name__, url_prefix='/user')

import app.user.user_api
