from app import app
from flask import render_template
from flask import request, flash, session
from flask import Blueprint
from .index_api import IndexAPI



@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template("index.html")

app.secret_key = '123456'