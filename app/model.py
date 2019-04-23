from flask import Flask
import datetime
from app import db
from flask_sqlalchemy import SQLAlchemy


class User(db.Model):

    __tablename__ = "ssmusic_user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(11), unique=True)
    info = db.Column(db.Text)
    sex = db.Column(db.Integer)
    uuid = db.Column(db.String(255), unique=True)
    userlog_id = db.Column(db.Integer)
    create_time = db.Column(db.DateTime, index=True, default=datetime.datetime.now())

    def __repr__(self):
        return "<User %r>" .format(self.name)


class UserLog(db.Model):

    __tablename__ = "ssmusic_userlog"

    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(100))
    do_what = db.Column(db.String(100))
    create_time = db.Column(db.DateTime, index=True, default=datetime.datetime.now())

    def __repr__(self):
        return "<Userlog %r>" .format(self.name)

class TestUser(db.Model):
    __tablename__ = "test_user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100))
    create_time = db.Column(db.DateTime, index=True, default=datetime.datetime.now())

    def __init__(self, name, pwd, create_time):
        self.name = name
        self.pwd = pwd
        self.create_time = create_time

    def __repr__(self):
        return "<TestUser %r>".format(self.name)

if __name__ == "__main__":
    db.create_all()