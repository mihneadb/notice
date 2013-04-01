from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'h4xxorz'
app.config['SECURITY_PASSWORD_HASH'] = 'bcrypt'
app.config['SECURITY_PASSWORD_SALT'] = app.config['SECRET_KEY']

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

app.config['SECURITY_POST_LOGIN'] = '/'

db = SQLAlchemy(app)

import notice.views
import notice.models
