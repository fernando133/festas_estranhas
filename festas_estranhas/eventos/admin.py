from django.contrib import admin
from .models import Evento

@admin.register(Evento)
class EventoInline(admin.ModelAdmin):
	list_display = ['id', 'descricao','responsavel', 'data_hora']
	search_fields = ['descricao']
	list_filter   = ('data_hora',)
