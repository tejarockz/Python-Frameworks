from flask import Flask
from logging import DEBUG

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = b'*[\x84\xab\x80\x08\xd2a'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

login_manager = LoginManager(app)

app.logger.setLevel(DEBUG)


from flask_package import routes