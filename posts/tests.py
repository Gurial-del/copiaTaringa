from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Post
from django.contrib.auth.models import User


class PostTests(APITestCase):
    def test_view_posts_anonymous(self):
        """
        Prueba que un usuario anónimo NO pueda ver los posts.
        """
        url = reverse('post-list') # Busca la URL de la lista de posts automáticamente
        response = self.client.get(url) # Intenta entrar (sin token)
        
        # Esperamos que el portero le diga "401 Unauthorized"
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        print("\n✅ Prueba 1: El portero detuvo al anónimo correctamente.")
# Create your tests here.

    # --- NUEVA PRUEBA ---
    def test_view_posts_authenticated(self):
        """
        Prueba que un usuario autenticado SÍ pueda ver los posts.
        """
        # 1. Crear un usuario de prueba en la DB temporal
        user = User.objects.create_user(username='testuser', password='testpassword')
        
        # 2. "Falsificar" el login (Le ponemos el brazalete VIP al cliente fantasma)
        self.client.force_authenticate(user=user)
        
        # 3. Hacer la petición
        url = reverse('post-list')
        response = self.client.get(url)
        
        # 4. El Juez verifica: Esperamos un 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print("\n✅ Prueba 2: El usuario autenticado entró correctamente.")