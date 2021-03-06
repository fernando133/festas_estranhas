from django.db import models
from eventos.models import Evento
from notificacoes.models import Email
from convidados.helpers.email_helper import EmailHelper

class Convidado(models.Model):
	id = models.BigAutoField(primary_key=True)
	nome = models.CharField(
		'Nome',
		help_text  = 'Nome completo',
		max_length = 200
	)

	e_mail = models.CharField(
		'E-mail',
		max_length = 300,
		help_text= 'Informe e-mail'
	)

	telefone = models.CharField(
		'Telefone',
		max_length = 300,
		help_text= 'Informe e-mail'
	)
	
	confirmou_presenca = models.BooleanField(
		'Confirmou presença?',
		default=False
	)

	evento = models.ForeignKey(
		Evento, 
		on_delete=models.CASCADE,
		blank=True
	)

	def __str__(self):
		return self.nome

	def save(self, *args, **kwargs):
		super(Convidado, self).save(*args, **kwargs)
		EmailHelper.email_convite(self)
		return self
	
	class Meta:
		verbose_name        = 'Convidado'
		verbose_name_plural = 'Convidados'
