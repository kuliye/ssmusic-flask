from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://xieliang:xieliang@47.101.39.239:3306/ssmusic"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["UP_DIR"] = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static/uploads/')

db = SQLAlchemy(app)
app.debug = True
app.template_folder = '../templates'
app.static_folder = '../static'

app.config['SECRET_KEY'] = '454'

from .index import index
from .user import user

app.register_blueprint(index, url_prefix='/')
app.register_blueprint(user, url_prefix='/user')


# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template("404.html"), 404



