from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import UserMixin

from notice import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    
    def __repr__(self):
        return "<Post {title}>".format(title=self.title)
    

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
