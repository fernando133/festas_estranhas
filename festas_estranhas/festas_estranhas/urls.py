from django.urls import include, path
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from rest_framework import viewsets
from convidados.api.viewsets import ConvidadoViewSet
from eventos.api.viewsets import EventoViewSet

router = routers.DefaultRouter()
#rotas app convidados
router.register(r'convidados', ConvidadoViewSet)
#rotas app eventos
router.register(r'eventos', EventoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
