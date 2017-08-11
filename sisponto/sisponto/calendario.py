from calendar import monthrange
from datetime import datetime, date

def monta_calendario(ano=None, mes=None):

	if ano is None:
		ano = datetime.now().year
	if mes is None:
		mes = datetime.now().month


	dias = monthrange(ano, mes)[1] + 1
	fim_de_semana = {6: 'Sábado', 7: 'Domingo'}
	calendario = {}

	for dia in range(1, dias):
		data = date(ano, mes, dia)

		if data.isoweekday() >= 6:
			calendario[dia] = fim_de_semana.get(data.isoweekday())
		else:
			calendario[dia] = ''

	return calendario