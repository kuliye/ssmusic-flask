from app import app
from flask import render_template

from flask import Blueprint



@app.route('/')
def index():
    return render_template("index.html")