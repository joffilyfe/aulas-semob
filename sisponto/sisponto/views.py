from flask import render_template, redirect, url_for, request, flash
from flask_login import login_required, login_user
from sisponto import login_manager, app as bp
from sisponto.models import Funcionario, Usuario
from sisponto.calendario import monta_calendario


@login_manager.user_loader
def load_user(id):
    return Usuario("Joffily")

@login_manager.unauthorized_handler
def unauthorized():
    flash("Por favor, faça o login")
    return redirect(url_for('login', next=request.url))

@bp.route('/')
@bp.route('/funcionario/<matricula>')
def index(matricula=None):

    if not matricula is None:
        funcionario = Funcionario.query.filter_by(
            matricula=matricula).first()
    else:
        funcionario = None

    return render_template('index.html',
        calendario=monta_calendario(),
        funcionario=funcionario)


@bp.route('/login', methods=['get', 'post'])
def login():
    if request.method == 'POST':
        login_user(Usuario("Joffily"))
        flash("Login realizado com sucesso")
        return redirect(request.args.get('next', '/'))

    return render_template('login.html')