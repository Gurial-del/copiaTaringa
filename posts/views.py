import logging
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated

logger = logging.getLogger(__name__)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()      # 1. ¿Qué datos busco? -> Todos los posts
    serializer_class = PostSerializer  # 2. ¿Cómo los traduzco? -> Usa mi serializerfrom django.shortcuts import render
    permission_classes = [IsAuthenticated]  # Requiere que el usuario esté autenticado
# Create your views here.
    # 3. Interceptamos la acción de "listar" para dejar un registro
    def list(self, request, *args, **kwargs):
        logger.info("👀 Alguien ha consultado los posts") # <--- El mensaje
        return super().list(request, *args, **kwargs) # Dejamos que Django siga con su trabajo normal