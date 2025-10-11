from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Post, Comment

User = get_user_model()

class PostsAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='u1', password='pass123')
        self.post = Post.objects.create(author=self.user, title='T1', content='C1')

    def test_list_posts(self):
        url = reverse('post-list')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_create_post_requires_auth(self):
        url = reverse('post-list')
        data = {'title': 'New', 'content': 'abc'}
        resp = self.client.post(url, data)
        self.assertIn(resp.status_code, (401, 403, 302))  # unauthenticated -> not allowed
        self.client.login(username='u1', password='pass123')
        resp = self.client.post(url, data)
        self.assertEqual(resp.status_code, 201)
