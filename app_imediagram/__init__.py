
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


app = Flask( __name__ )

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'
app.config['SECRET_KEY'] = 'afaa11fcf8bc5683ef530de6cebfb44c'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
loggin_manager = LoginManager(app)


loggin_manager.login_view = "homepage"

from app_imediagram import routes