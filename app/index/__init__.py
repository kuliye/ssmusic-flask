from flask import Blueprint

index = Blueprint("index", __name__, url_prefix='/')

import app.index.index_api
import app.index.index_views
