from rest_framework import viewsets
from convidados.api.serializers import ConvidadoSerializer
from convidados.models import Convidado
from eventos.models import Evento
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

class ConvidadoViewSet(viewsets.ModelViewSet):
	"""
	Endpoint que permite manter convidados.
	"""
	serializer_class = ConvidadoSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['evento']

	def get_queryset(self):
		return Convidado.objects.all().order_by('nome')
