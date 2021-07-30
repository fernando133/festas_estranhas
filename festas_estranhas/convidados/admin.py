from django.contrib import admin
from .models import Convidado

@admin.register(Convidado)
class ConvidadoInline(admin.ModelAdmin):
	list_display = ['id', 'nome', 'e_mail', 'telefone', 'confirmou_presenca']
	search_fields = ['nome', 'e-mail']
	list_filter   = ('confirmou_presenca',)

