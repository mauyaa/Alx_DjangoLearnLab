from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

class PostCommentTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.client.post('/api/accounts/register/', {'username': 'alice', 'password': 'password123'})
        login = self.client.post('/api/accounts/login/', {'username': 'alice', 'password': 'password123'})
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + login.data['token'])

    def test_create_post_comment_like(self):
        p = self.client.post('/api/posts/posts/', {'title': 'Hello', 'content': 'World'})
        self.assertEqual(p.status_code, status.HTTP_201_CREATED)
        post_id = p.data['id']

        c = self.client.post('/api/posts/comments/', {'post': post_id, 'content': 'Nice!'})
        self.assertEqual(c.status_code, status.HTTP_201_CREATED)

        like = self.client.post(f'/api/posts/posts/{post_id}/like/')
        self.assertEqual(like.status_code, status.HTTP_200_OK)
