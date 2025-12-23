from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views  # Importamos tus vistas desde views.py

# 1. Configuración del Router para la API
router = DefaultRouter()
router.register(r'api/posts', views.PostViewSet, basename='post')

# 2. Definición de URLs
urlpatterns = [
    # --- Vistas Normales (HTML) ---
    path('', views.feed, name='feed'),           # La portada (feed)
    path('login/', views.login_view, name='login'), # El login

    # --- API (JSON) ---
    # El router genera URLs como: /api/posts/, /api/posts/1/, etc.
    path('', include(router.urls)), 
]