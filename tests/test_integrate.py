from selenium.webdriver.common.keys import Keys
from django.urls import reverse
from django.contrib.auth.models import User
from proj_app.models import Session

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import time
from django.contrib.auth.models import Group

class Tests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        cls.selenium.implicitly_wait(10)
        cls.group = Group.objects.create(name='Players')
    
    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()
    
    def test_a_registration(self):
        self.selenium.get(f'{self.live_server_url}/accounts/register')
        self.selenium.find_element(By.ID, 'id_username').send_keys('tempuser')
        self.selenium.find_element(By.ID, 'id_email').send_keys('tu@email.com')
        self.selenium.find_element(By.ID, 'id_password1').send_keys('#EDC1qaz')
        self.selenium.find_element(By.ID, 'id_password2').send_keys('#EDC1qaz')
        self.selenium.find_element(By.NAME, 'Create User').click()

        success_message = self.selenium.find_element(By.CLASS_NAME, 'alert-success')
        self.assertEqual(success_message.text, 'Account was created for tempuser')

    def test_b_login(self):
        User.objects.create_user(username='tempuser', password='#EDC1qaz')
        self.selenium.get(f'{self.live_server_url}/accounts/login')
        self.selenium.find_element(By.ID, 'id_username').send_keys('tempuser')
        self.selenium.find_element(By.ID, 'id_password').send_keys('#EDC1qaz')
        self.selenium.find_element(By.NAME, 'Login').click()
        self.assertTrue(self.selenium.current_url == f'{self.live_server_url}/')

    def test_c_create_session(self):
        User.objects.create_user(username='tempuser', password='#EDC1qaz')
        self.selenium.get(f'{self.live_server_url}/accounts/login')
        self.selenium.find_element(By.ID, 'id_username').send_keys('tempuser')
        self.selenium.find_element(By.ID, 'id_password').send_keys('#EDC1qaz')
        self.selenium.find_element(By.NAME, 'Login').click()
        self.selenium.get(f'{self.live_server_url}/session/create')
        self.selenium.find_element(By.ID, 'id_title').send_keys('Session 1')
        self.selenium.execute_script("document.getElementById('id_game_name').value = 'Game1'")
        self.selenium.execute_script("document.getElementById('id_thumbnail').value = 'https://www.example.com'")
        self.selenium.find_element(By.ID, 'id_date').send_keys('2024-04-26')
        self.selenium.find_element(By.ID, 'id_time').send_keys('12:00:00')
        self.selenium.find_element(By.ID, 'id_description').send_keys('Description')
        self.selenium.find_element(By.NAME, 'submit').click()
        self.assertTrue(self.selenium.current_url == f'{self.live_server_url}/listings/')

    def test_d_logout(self):
        User.objects.create_user(username='tempuser', password='#EDC1qaz')
        self.selenium.get(f'{self.live_server_url}/accounts/login')
        self.selenium.find_element(By.ID, 'id_username').send_keys('tempuser')
        self.selenium.find_element(By.ID, 'id_password').send_keys('#EDC1qaz')
        self.selenium.find_element(By.NAME, 'Login').click()
        self.selenium.find_element(By.NAME, 'logout').click()
        self.assertTrue(self.selenium.current_url == f'{self.live_server_url}/accounts/logout/')