from django.shortcuts import render
from rest_framework import viewsets
from convidados.serializers import ConvidadoSerializer
from .models import Convidado

class ConvidadoViewSet(viewsets.ModelViewSet):
	"""
	Endpoint que permite listar e adicionar convidados
	"""
	serializer_class = ConvidadoSerializer
	queryset = Convidado.objects.all().order_by('nome')
	