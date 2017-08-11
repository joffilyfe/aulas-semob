from os import urandom
from flask import Flask
from flask_login import LoginManager, login_user, login_required
from flask_sqlalchemy import SQLAlchemy

app = Flask('sisponto')
app.config['SQLALCHEMY_DATABASE_URI'] = "firebird+fdb://sysdba:pw@10.40.0.2:3050//database/ponto.fdb?charset=ISO8859_1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = urandom(32)


db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.setup_app(app)


from sisponto import views