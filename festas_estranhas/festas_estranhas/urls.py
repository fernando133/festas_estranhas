from django.urls import include, path
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from rest_framework import viewsets
from rest_framework.authtoken import views
from eventos.api.viewsets import EventoViewSet
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt import views as jwt_views
from convidados.api.viewsets import ConvidadoViewSet, ConfirmarPresencaViewSet

router = routers.DefaultRouter()
#rotas app convidados
router.register(r'convidados', ConvidadoViewSet, basename='Convidado')
router.register(r'presencaconvidado', ConfirmarPresencaViewSet, basename='ConfirmarPresenca')

#rotas app eventos
router.register(r'eventos', EventoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
