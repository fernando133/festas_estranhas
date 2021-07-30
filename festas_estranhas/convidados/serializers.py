from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Convidado

class ConvidadoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Convidado
		fields = ['id', 'nome', 'e_mail', 'telefone']