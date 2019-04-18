from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:xieliang@127.0.0.1:3306/ssmusic"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["UP_DIR"] = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static/uploads/')

db = SQLAlchemy(app)
app.debug = True
app.template_folder = '../templates'
app.template_folder = '../static'

app.config['SECRET_KEY'] = '454'





from app.home import home as home_blueprint
from app.user import user as user_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(user_blueprint)

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.route('/')
def index():
    return render_template("index.html")