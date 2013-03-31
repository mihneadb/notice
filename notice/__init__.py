from flask import Flask

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'h4xxorz'
app.config['SECURITY_PASSWORD_HASH'] = 'bcrypt'
app.config['SECURITY_PASSWORD_SALT'] = app.config['SECRET_KEY']

app.config['SECURITY_POST_LOGIN'] = '/'

import notice.views
import notice.models
