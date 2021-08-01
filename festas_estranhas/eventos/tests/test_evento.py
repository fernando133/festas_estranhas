import pytest
from eventos.models import Evento 
import datetime
from mixer.backend.django import mixer
from django.utils import timezone

@pytest.mark.django_db
class TestModels:
	def test_post_create(self):
		evento = Evento.objects.create(
			descricao = 'Hogwards',
			responsavel='Harry Potter',
			email_responsavel='fernando.gmp@gmail.com',
			data_hora=datetime.datetime.now(tz=timezone.utc)
		)
	
	def test_model_display_title(self):
		evento = mixer.blend(Evento, descricao='Copa de Quadri-ball')
		assert str(evento) == 'Copa de Quadri-ball'