from django.db import models
import os
from twilio.rest import Client

class SMS:
	"""
	Envia SMS por meio de integracao com a plataforma Twiliio
	"""
	def __init__(self):
		self.account_sid = os.environ['TWILIO_ACCOUNT_SID']
		self.auth_token = os.environ['TWILIO_AUTH_TOKEN']
		self.remetente = os.environ['REMETENTE']
		self.client = Client(self.account_sid, self.auth_token)

	def enviar(self, conteudo, destinatario):
		try:
			message = self.client.messages.\
				create(
					body=conteudo,
					from_=self.remetente,
					to=destinatario
				)
			return message.sid
		except Exception as e:
			return "Erro SMS: " + str(e)
