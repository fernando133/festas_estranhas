from django.contrib import admin
from .models import Evento

@admin.register(Evento)
class EventoInline(admin.ModelAdmin):
	list_display = ['id', 'descricao', 'data']
	search_fields = ['descricao']
	list_filter   = ('data',)
