from flask import Flask
import datetime
from app import db
from flask_sqlalchemy import SQLAlchemy


class User(db.Model):

    __tablename__ = "ssmusic_user"
    __table_args__ = {"useexisting": True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    pwd = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(11), unique=True)
    info = db.Column(db.Text)
    gender = db.Column(db.Integer)
    uuid = db.Column(db.String(255), unique=True)
    create_time = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, user_dict):
        self.name = user_dict['name']
        self.pwd = user_dict['password']
        self.email = user_dict['email']
        self.phone = user_dict['phone']
        self.gender = user_dict['gender']
        self.uuid = user_dict['uuid']
        self.create_time = datetime.datetime.now()

    def __repr__(self):
        return "<User %r>" .format(self.name)


class UserLog(db.Model):

    __tablename__ = "ssmusic_userlog"
    __table_args__ = {"useexisting": True}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    ip = db.Column(db.String(100))
    do_what = db.Column(db.String(100))
    create_time = db.Column(db.DateTime, index=True, default=datetime.datetime.now())


    def __repr__(self):
        return "<Userlog %r>" .format(self.name)

class TestUser(db.Model):
    __tablename__ = "test_user"
    __table_args__ = {"useexisting": True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100))
    create_time = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, user_dict):
        self.name = user_dict['name']
        self.pwd = user_dict['password']
        self.create_time = datetime.datetime.now()

    def __repr__(self):
        return "<TestUser %r>".format(self.name)

if __name__ == "__main__":
    db.create_all()