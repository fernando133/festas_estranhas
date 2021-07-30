from rest_framework import viewsets
from convidados.api.serializers import ConvidadoSerializer
from convidados.models import Convidado
from eventos.models import Evento
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

class ConvidadoViewSet(viewsets.ModelViewSet):
	"""
	Endpoint que permite listar e adicionar convidados.
	"""
	serializer_class = ConvidadoSerializer
	queryset = Convidado.objects.all().order_by('nome')
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['evento', 'confirmou_presenca']
