from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class TestSignupView(TestCase):

    def setUp(self) -> None:
        self.valid_data = {
            'username': 'testuser',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'testuser@example.com',
            'address': '123 Main St',
            'password1': 'testpassword123',
            'password2': 'testpassword123'

        }
        self.bad_data = {
            'username': 'testuser',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'testuser@example.com',
            'address': '123 Main St',
            'password1': 'testpassword123',
            'password2': 'otherpassword',
        }
    def test_signup_view_sucessful(self):
        response = self.client.post(reverse('signup'), self.valid_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))
        self.assertTrue(User.objects.filter(username='testuser').exists())
        
        

    def test_signup_invalid(self):
        msg = "<li>Los dos campos de contrase"
        response = self.client.post(reverse('signup'), self.bad_data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username='testuser').exists())
        self.assertTrue(msg in str(response.content))
        # print("*" * 28)
        # print(response.content)
        
class TestLoginView(TestCase):
    def test_login_view_get(self):

        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], AuthenticationForm)

    def test_login_view_post(self):
        User.objects.create_user(username='testuser', password='testpassword')

        login_data = {
            'username': 'testuser',
            'password': 'testpassword',
        }

        # Realiza una solicitud POST con los datos de inicio de sesión
        response = self.client.post(reverse('login'), data=login_data, follow=True)
        self.assertRedirects(response, reverse('index'))
        self.assertTrue(response.context['user'].is_authenticated)
