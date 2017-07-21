from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, request
from calendario import monta_calendario

app = Flask('sisponto')
app.config['SQLALCHEMY_DATABASE_URI'] = "firebird+fdb://user:senha@ip:porta//database/ponto.fdb?charset=ISO8859_1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Funcionario(db.Model):
	id = db.Column('fun_codigo', db.Integer, primary_key=True)
	matricula = db.Column('fun_matricula', db.Integer)
	nome = db.Column('fun_nome', db.String)

	def __repr__(self):
		return f'<Funcionario: {self.nome}>'

@app.route('/')
@app.route('/funcionario/<matricula>')
def index(matricula=None):

	if not matricula is None:
		funcionario = Funcionario.query.filter_by(
			matricula=matricula).first()
	else:
		funcionario = None

	return render_template('index.html',
		calendario=monta_calendario(),
		funcionario=funcionario)