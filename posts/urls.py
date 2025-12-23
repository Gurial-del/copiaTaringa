from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

# Creamos el Router
router = DefaultRouter()
# Le decimos: "Maneja la ruta 'posts' usando el PostViewSet"
router.register(r'posts', PostViewSet)

urlpatterns = [
    # Incluimos todas las rutas que el router generó automáticamente
    path('', include(router.urls)),
]