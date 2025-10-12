from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

class AuthTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_register_and_login(self):
        r = self.client.post(reverse('register'), {'username': 'alice', 'password': 'password123'})
        self.assertEqual(r.status_code, status.HTTP_201_CREATED)
        token = r.data['token']
        self.assertTrue(token)

        r2 = self.client.post(reverse('login'), {'username': 'alice', 'password': 'password123'})
        self.assertEqual(r2.status_code, status.HTTP_200_OK)
        self.assertIn('token', r2.data)
