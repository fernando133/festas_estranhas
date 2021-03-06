from django.contrib.auth.models import User, Group
from rest_framework import serializers
from convidados.models import Convidado
from eventos.api.serializers import EventoSerializer

class ConvidadoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Convidado
		fields = ['id', 'nome', 'e_mail', 'telefone', 'evento', 'confirmou_presenca']
		