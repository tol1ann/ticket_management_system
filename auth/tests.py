from rest_framework.test import APITestCase

from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth.models import User
from django.urls import reverse


class AuthenticationAPITestCase(APITestCase):
    def test_user_registration(self):
        registration_data = {
            'username': 'testuser',
            'email': 'test5@test5.com',
            'password': 'testpassword123',
            'password_repeated': 'testpassword123',
            'first_name': 'test',
            'last_name': 'user'
        }

        response = self.client.post(reverse('auth_register'), data=registration_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_user_login(self):
        user = User.objects.create_user(username='testuser', password='testpassword123')

        login_data = {
            'username': 'testuser',
            'password': 'testpassword123',
        }

        response = self.client.post(reverse('token_login'), data=login_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

        refresh = response.data['refresh']
        refresh_token = RefreshToken(refresh)

        response = self.client.post(reverse('token_refresh'), data={'refresh': refresh})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

        access_token_after_refresh = response.data['access']
        access_token = str(refresh_token.access_token)

        self.assertNotEqual(access_token, access_token_after_refresh)