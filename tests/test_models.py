from django.test import TestCase
from django.contrib.auth.models import User
from proj_app.models import Session

class SessionModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.session = Session.objects.create(
            owner=self.user,
            title='Test Session',
            game_name='Test Game',
            thumbnail='https://test.com',
            date='2024-04-24',
            time='12:00:00',
            description='Test Description'
        )
    
    def test_title(self):
        session = Session.objects.get(id=1)
        expected_object_name = f'{session.title}'
        self.assertEqual(expected_object_name, 'Test Session')
    
    def test_game_name(self):
        session = Session.objects.get(id=1)
        expected_object_name = f'{session.game_name}'
        self.assertEqual(expected_object_name, 'Test Game')

    def test_thumbnail(self):
        session = Session.objects.get(id=1)
        expected_object_name = f'{session.thumbnail}'
        self.assertEqual(expected_object_name, 'https://test.com')

    def test_date(self):
        session = Session.objects.get(id=1)
        expected_object_name = f'{session.date}'
        self.assertEqual(expected_object_name, '2024-04-24')

    def test_time(self):
        session = Session.objects.get(id=1)
        expected_object_name = f'{session.time}'
        self.assertEqual(expected_object_name, '12:00:00')

    def test_description(self):
        session = Session.objects.get(id=1)
        expected_object_name = f'{session.description}'
        self.assertEqual(expected_object_name, 'Test Description')
