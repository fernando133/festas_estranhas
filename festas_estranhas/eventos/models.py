from django.db import models
from datetime import date, datetime

class Evento(models.Model):
	id = models.BigAutoField(primary_key=True)

	descricao = models.CharField(
		'Descrição',
		help_text  = 'Descrição do evento',
		max_length = 200
	)

	responsavel = models.CharField(
		'Resposável pelo evento',
		help_text="Nome do responsável pelo evento",		
		max_length=200
	)

	email_responsavel = models.EmailField(
		'Email',
		help_text="Email do responsável pelo evento",		
		max_length=200
	)

	data_hora = models.DateTimeField(
		'Data e Hora',
		help_text  = 'Data e hora do evento',
	)

	def __str__(self):
		return self.descricao

	class Meta:
		verbose_name        = 'Evento'
		verbose_name_plural = 'Eventos'
