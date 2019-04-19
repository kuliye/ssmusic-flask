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
    face = db.Column(db.String(255), unique=True)
    uuid = db.Column(db.String(255), unique=True)
    userlog = db.relationship('UserLog', backref='ssmusic_user')
    create_time = db.Column(db.DateTime, index=True, default=datetime.datetime.now())

    def __repr__(self):
        return "<User %r>" .format(self.name)


class UserLog(db.Model):

    __tablename__ = "ssmusic_userlog"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('ssmusic_user.id'))
    ip = db.Column(db.String(100))
    do_what = db.Column(db.String(100))
    create_time = db.Column(db.DateTime, index=True, default=datetime.datetime.now())

    def __repr__(self):
        return "<Userlog %r>" .format(self.name)

if __name__ == "__main__":
    db.create_all()