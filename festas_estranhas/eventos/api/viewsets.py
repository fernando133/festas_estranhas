from eventos.models import Evento
from rest_framework import viewsets
from rest_framework.response import Response
from eventos.api.serializers import EventoSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend

class EventoViewSet(viewsets.ModelViewSet):
	"""
	Endpoint que permite manter eventos.
	"""

	permission_classes = [IsAuthenticated, IsAdminUser]
	authentication_classes = [TokenAuthentication,]
	serializer_class = EventoSerializer
	queryset = Evento.objects.all().order_by('id')
	