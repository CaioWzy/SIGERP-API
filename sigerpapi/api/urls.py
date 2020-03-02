from django.urls import include, path
from rest_framework import routers
from sigerpapi.api import views

router = routers.DefaultRouter()
router.register(r'clientes', views.ClienteViewSet)
router.register(r'funcionarios', views.FuncionarioViewSet)
router.register(r'escalas', views.FuncionarioEscalaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]