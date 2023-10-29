from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class TestLoginView(TestCase):
    def test_login_view_get(self):
        # Realiza una solicitud GET a la vista de inicio de sesión
        response = self.client.get(reverse('login'))

        # Verifica que la página de inicio de sesión devuelva un código de estado 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Verifica que el formulario de inicio de sesión se muestre en la respuesta
        self.assertIsInstance(response.context['form'], AuthenticationForm)

    def test_login_view_post(self):
        # Crea un usuario de prueba para usar en la prueba de inicio de sesión
        User.objects.create_user(username='testuser', password='testpassword')

        # Datos de prueba para el inicio de sesión
        login_data = {
            'username': 'testuser',
            'password': 'testpassword',
        }

        # Realiza una solicitud POST con los datos de inicio de sesión
        response = self.client.post(reverse('login'), data=login_data, follow=True)

        # Verifica que la página redirija al usuario después del inicio de sesión
        self.assertRedirects(response, reverse('index'))

        # Verifica que el usuario esté autenticado después del inicio de sesión
        self.assertTrue(response.context['user'].is_authenticated)
