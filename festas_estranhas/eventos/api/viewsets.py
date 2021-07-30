from rest_framework import viewsets
from eventos.api.serializers import EventoSerializer
from eventos.models import Evento
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

class EventoViewSet(viewsets.ModelViewSet):
	"""
	Endpoint que permite manter eventos.
	"""
	serializer_class = EventoSerializer
	queryset = Evento.objects.all().order_by('id')
	