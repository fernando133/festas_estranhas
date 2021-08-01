import os
import json
import smtplib, ssl
from django.db import models
from threading import Thread
from twilio.rest import Client
from email.mime.text import MIMEText
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from email.message import EmailMessage

class SMS:
	"""
	Envia SMS por meio de integracao com a plataforma Twiliio
	"""
	def __init__(self):
		self.account_sid = os.environ['TWILIO_ACCOUNT_SID']
		self.auth_token = os.environ['TWILIO_AUTH_TOKEN']
		self.remetente = os.environ['REMETENTE']
		self.client = Client(self.account_sid, self.auth_token)

	@staticmethod
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

class EmailSendGrid:
	"""
	Envia e-mails por meio de integracao com a api sendgrid
	"""
	def __init__(self):
		self.sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
	
	@staticmethod
	def enviar (self, from_email, to_emails, subject, html_content):
		try:
			message = Mail(
				from_email = from_email,
				to_emails = to_emails,
				subject = subject,
				html_content = html_content
			)

			response = self.sg.send(message)
			return response.headers
		except Exception as e:
			return "Erro: " + str(e)

class Email(Thread):
	def __init__(self, emails, assunto, conteudo):
		Thread.__init__(self)
		self.emails = emails
		self.assunto = assunto
		self.conteudo = conteudo
		self.smtp_server = os.environ['SMTP_SERVER']
		self.port = os.environ['SMTP_PORT']
		self.sender_email = os.environ['SENDER_EMAIL']
		self.sender_password = os.environ['SENDER_PASSWORD']
		self.context = ssl.create_default_context()
	
	def get_server(self):
		try:
			self.server = smtplib.SMTP(self.smtp_server, self.port)
			self.server.starttls(context=self.context)
			self.server.login(self.sender_email, self.sender_password)
		except Exception as e:
			return "Erro: " + str(e)

	def run(self):
		mensagem = EmailMessage()
		mensagem.set_content(self.conteudo, 'html')
		mensagem['Subject'] = self.assunto
		mensagem['From'] = self.sender_email
		mensagem['To'] = self.emails
		self.get_server()
		try:
			self.server.send_message(mensagem)
			return 200
		except Exception as e:
			return "Erro: "+str(e)
		finally:
			self.server.quit()

	def enviar(self):
		return self.start()
