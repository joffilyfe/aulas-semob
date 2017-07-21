from . import db


class Cargo(db.Model):
	__tablename__ = 'cargos'

	id = db.Column('car_codigo', db.Integer, primary_key=True)
	nome = db.Column('car_descricao', db.String)

	def __repr__(self):
		return f"<Cargo: {self.nome}>"

	def __str__(self):
		return f"{self.nome}"


class Setor(db.Model):
	__tablename__ = 'setor'
	
	id = db.Column('set_codigo', db.Integer, primary_key=True)
	nome = db.Column('set_descricao', db.String)

	def __repr__(self):
		return f"<Setor: {self.nome}>"

	def __str__(self):
		return f"{self.nome}"


class Funcionario(db.Model):
	__tablename__ = 'funcionario'

	id = db.Column('fun_codigo', db.Integer, primary_key=True)
	matricula = db.Column('fun_matricula', db.Integer, nullable=False)
	nome = db.Column('fun_nome', db.String, nullable=False)
	setor_id = db.Column('fun_ce_setor', db.Integer, db.ForeignKey('setor.set_codigo'))
	setor = db.relationship('Setor', foreign_keys=[setor_id])
	cargo_id = db.Column('fun_ce_cargo', db.Integer, db.ForeignKey('cargos.car_codigo'))
	cargo = db.relationship('Cargo', foreign_keys=[cargo_id])

	def __repr__(self):
		return f"<Funcionario {self.matricula}:{self.nome}>"

	def __str__(self):
		return f"matrícula: {self.matricula}, nome: {self.nome}"