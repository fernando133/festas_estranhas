from convidados.models import Convidado
from convidados.helpers.email_helper import EmailHelper

class ConvidadoHelper:

	@staticmethod
	def informar_presenca(self, convidado):
		EmailHelper.email_convidado_confirmado(convidado)

	@staticmethod
	def confirmar_presenca(self, pk_convidado):
		try:
			convidado = Convidado.objects.get(id=pk_convidado)
			convidado.confirmou_presenca = True
			convidado.save()
			msg = "Presença confimada para " + convidado.nome
			ConvidadoHelper.informar_presenca(self, convidado)
			return msg
		except Exception as e:
			return "Erro: " + str(e)
