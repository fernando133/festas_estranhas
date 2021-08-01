from django.contrib.auth.models import User, Group
from rest_framework import serializers
from eventos.models import Evento

class EventoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Evento
		fields = ['id', 'descricao', 'responsavel', 'email_responsavel', 'data_hora']
