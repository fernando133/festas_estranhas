from eventos.models import Evento
from rest_framework import viewsets
from convidados.models import Convidado
from rest_framework.response import Response
from rest_framework.decorators import action
from convidados.api.serializers import ConvidadoSerializer
from django_filters.rest_framework import DjangoFilterBackend
from convidados.helpers.convidado_helper import ConvidadoHelper

class ConvidadoViewSet(viewsets.ModelViewSet):
	"""
	Endpoint que permite manter convidados.
	"""
	serializer_class = ConvidadoSerializer
	filter_backends = [DjangoFilterBackend]
	filterset_fields = ['evento']

	def get_queryset(self):
		return Convidado.objects.all().order_by('nome')
	
	@action(methods=['get'], detail=True)
	def confirmarpresenca(self, request, pk=None):
		"""
		Action que permite o convidado confirmar presença a partir de um
		link no e-mail de confirmação que o mesmo recebe ao ser cadastrado.
		"""
		response = ConvidadoHelper.confirmar_presenca(self,pk)
		return Response({'Response' : response})
