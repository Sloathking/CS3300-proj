from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from proj_app.models import Session

class ViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('testuser', 'password123')
        self.session = Session.objects.create(
            owner=self.user,
            title='test session',
            game_name='test game',
            thumbnail='test thumbnail',
            date='2024-04-24',
            time='12:00',
            description='test description'
        )
    
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'proj_app/index.html')
    
    def test_listings_view(self):
        response = self.client.get(reverse('listings'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'proj_app/listings.html')

    def test_sessionDetails_view(self):
        response = self.client.get(reverse('sessionDetails', args=[self.session.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'proj_app/session_details.html')
    
    def test_sessionUpdate_view(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('sessionUpdate', args=[self.session.id]))
        self.assertEqual(response.status_code, 302)
    
    def test_sessionDelete_view(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('sessionDelete', args=[self.session.id]))
        self.assertEqual(response.status_code, 302)
    
    def test_sessionCreate_view(self):
        self.client.login(username='testuser', password='password123')
        response = self.client.get(reverse('sessionCreate'))
        self.assertEqual(response.status_code, 302)
    
    def test_registerPage_view(self):
        response = self.client.get(reverse('registerPage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')