from django.urls import include, path
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from rest_framework import viewsets
from convidados.views import ConvidadoViewSet

router = routers.DefaultRouter()
router.register(r'convidados', ConvidadoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
