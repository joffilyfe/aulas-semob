from flask import render_template, url_for, request
from .utils.calendario import monta_calendario
from .models import Funcionario, Setor
from . import app


@app.route('/')
@app.route('/<matricula>')
def index(matricula=None):
	if matricula is None:
		funcionario = Funcionario.query.limit(1).all()[0]
	else:	
		funcionario = Funcionario.query.filter_by(matricula=matricula).first()

	return render_template('index.html',
		calendario=monta_calendario(), funcionario=funcionario)


@app.route('/user/add/<name>/<email>')
def add_user(name, email):
	user = User(name, email)
	db.session.add(user)
	db.session.commit()

	return 'Its ok'

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		print('ok')
		if request.form['password'] == '':
			return 'Senha inválida'

	return render_template('login.html')