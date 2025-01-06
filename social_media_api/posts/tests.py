from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Post, Like
from notifications.models import Notification

User = get_user_model()

class PostTests(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password1')
        self.user2 = User.objects.create_user(username='user2', password='password2')
        self.post = Post.objects.create(author=self.user1, title='Test Post', content='Test Content')

    def test_like_post(self):
        self.client.login(username='user2', password='password2')
        url = reverse('post-like', args=[self.post.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Like.objects.filter(post=self.post, user=self.user2).exists())
        self.assertTrue(Notification.objects.filter(recipient=self.user1, actor=self.user2, verb='liked your post').exists())

    def test_unlike_post(self):
        self.client.login(username='user2', password='password2')
        Like.objects.create(post=self.post, user=self.user2)
        url = reverse('post-unlike', args=[self.post.id])
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Like.objects.filter(post=self.post, user=self.user2).exists())

    def test_view_notifications(self):
        self.client.login(username='user1', password='password1')
        Notification.objects.create(recipient=self.user1, actor=self.user2, verb='liked your post', target=self.post)
        url = reverse('notification-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
