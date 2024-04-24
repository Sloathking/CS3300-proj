from django.test import TestCase
from django.contrib.auth.models import User
from proj_app.models import Session
from proj_app.forms import *

class SessionFormTest(TestCase):
    def test_form_fields(self):
        form = SessionForm()
        self.assertTrue(form.fields['title'])
        self.assertTrue(form.fields['game_name'])
        self.assertTrue(form.fields['thumbnail'])
        self.assertTrue(form.fields['date'])
        self.assertTrue(form.fields['time'])
        self.assertTrue(form.fields['description'])
    
class GameSelectFormTest(TestCase):
    def test_form_fields(self):
        form = GameSelectForm()
        self.assertTrue(form.fields['game_choices'])

class CreateUserFormTest(TestCase):
    def test_form_fields(self):
        form = CreateUserForm()
        self.assertTrue(form.fields['username'])
        self.assertTrue(form.fields['email'])
        self.assertTrue(form.fields['password1'])
        self.assertTrue(form.fields['password2'])
