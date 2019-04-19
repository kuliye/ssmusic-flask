from flask import Blueprint

user = Blueprint("user", __name__)

import app.user.user_api
