import pytest
import requests
from eventos.models import Evento 
from django.utils import timezone
from mixer.backend.django import mixer
from convidados.models import Convidado

@pytest.mark.django_db
class TestModels:
	def test_post_create(self):
		evento = Evento.objects.create(
			descricao = 'Hogwards',
			responsavel='Harry Potter',
			email_responsavel='fernando.gmp@gmail.com',
			data_hora=timezone.now()
		)

		convidado = Convidado.objects.create(
			nome = "Albus Dumbledore",
			telefone="6233131929",
			e_mail="fernando.gmp@gmail.com",
			confirmou_presenca = False,
			evento = evento
		)

	def test_model_display_title(self):
		convidado = mixer.blend(Convidado, nome='Hermione')
		assert str(convidado) == 'Hermione'
		