from django.db import models

class Evento(models.Model):
	id = models.BigAutoField(primary_key=True)

	descricao = models.CharField(
		'Descrição',
		help_text  = 'Descrição do evento',
		max_length = 200
	)

	data = models.DateField(
		'Data',
		help_text  = 'Data do evento',
	)

	def __str__(self):
		return self.descricao

	class Meta:
		verbose_name        = 'Evento'
		verbose_name_plural = 'Eventos'