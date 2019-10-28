from django.urls import resolve
from django.test import TestCase

from private_profiles.views import register, profiles_developer


class RegisterPageTest(TestCase):

    def test_register_url_returns_register_view(self):
        found = resolve('/register/')  
        self.assertEqual(found.func, register)

    def test_register_page_returns_correct_html(self):
        response = self.client.get('/register/')
        self.assertTemplateUsed(response, 'private_profiles/register.html', 'public_profiles/base.html')



class ProfilesPageTest(TestCase):

    def test_profiles_developer_url_returns_profiles_developer_view(self):
        found = resolve('/profiles_developer/')  
        self.assertEqual(found.func, profiles_developer)

    def test_profiles_developer_page_returns_correct_html(self):
        response = self.client.get('/profiles_developer/')
        self.assertTemplateUsed(response, 'private_profiles/profiles_developer.html', 'public_profiles/base.html')
        # This test is failing - "AssertionError: No templates used to render the response"



class LoginPageTest(TestCase):

    def test_login_url_returns_login_page(self):
        found = resolve('/login/')  
        # self.assertEqual(found.func, register)  -- or should we create a view for login too???

    def test_login_page_returns_correct_html(self):
        response = self.client.get('/login/')
        self.assertTemplateUsed(response, 'private_profiles/login.html', 'public_profiles/base.html')


class LogoutPageTest(TestCase):

    def test_logout_url_returns_logout_page(self):
        found = resolve('/logout/')  
        # self.assertEqual(found.func, register)  -- or should we create a view for logout too???

    def test_logout_page_returns_correct_html(self):
        response = self.client.get('/logout/')
        self.assertTemplateUsed(response, 'private_profiles/logout.html', 'public_profiles/base.html')