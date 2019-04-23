from flask import Blueprint

user = Blueprint("user", __name__)

import app.user.user_api
import app.user.user_view
