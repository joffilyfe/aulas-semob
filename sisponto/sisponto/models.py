from sisponto import db


class Funcionario(db.Model):
	id = db.Column('fun_codigo', db.Integer, primary_key=True)
	matricula = db.Column('fun_matricula', db.Integer)
	nome = db.Column('fun_nome', db.String)

	def __repr__(self):
		return f'<Funcionario: {self.nome}>'


class Usuario():
	def __init__(self, login):
		self.id = 1
		self.login = login
		self.is_active = True

	def __str__(self):
		return f"<Usuario {self.login}>"

	def get_id(self):
		return self.id

	def is_authenticated(self):
		return True
