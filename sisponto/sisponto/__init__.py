import os
from flask import Flask, g, session
from flask_sqlalchemy import SQLAlchemy
from flask_simpleldap import LDAP


app = Flask('sisponto')
app.config.from_object('sisponto')

app.config.update(dict(
	SECRET_KEY=os.urandom(10),
	SQLALCHEMY_TRACK_MODIFICATIONS = False,
	DEBUG=True,
	SQLALCHEMY_DATABASE_URI = f"firebird+fdb://sysdba:{os.environ.get('PONTO_DB_PASS')}@10.40.0.5:3050//database/ponto.fdb?charset=ISO8859_1"),
)

db = SQLAlchemy(app)

# g.user = {}
@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        g.user = {}