import logging
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import Post
from .serializers import PostSerializer

logger = logging.getLogger(__name__)

# ---------------------------------------------------------
# BLOQUE 1: API (Para que consuman datos JSON)
# ---------------------------------------------------------
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()      # 1. ¿Qué datos busco? -> Todos los posts
    serializer_class = PostSerializer  # 2. ¿Cómo los traduzco? -> Usa mi serializer
    permission_classes = [IsAuthenticated]  # Requiere que el usuario esté autenticado

    # 3. Interceptamos la acción de "listar" para dejar un registro
    def list(self, request, *args, **kwargs):
        logger.info("👀 Alguien ha consultado los posts vía API") 
        return super().list(request, *args, **kwargs) 

# ---------------------------------------------------------
# BLOQUE 2: VISTAS NORMALES (Para devolver HTML al navegador)
# ---------------------------------------------------------

# 1. VISTA DEL FEED (Home)
# Nota: Esta función está FUERA de la clase PostViewSet
def feed(request):
    # "Traeme todos los posts, ordenados del más nuevo al más viejo"
    posts = Post.objects.all().order_by('-fecha_creacion')
    
    context = {
        'lista_posts': posts,
        'titulo_pagina': 'CopiaTaringa - Inteligencia Colectiva'
    }
    return render(request, 'posts/feed.html', context)

# 2. VISTA DE LOGIN
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('feed')
    else:
        form = AuthenticationForm()
    return render(request, 'posts/login.html', {'form': form})