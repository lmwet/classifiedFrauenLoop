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


    def test_logged_in_user_can_see_logout_link(self):

        class MockUser:
            is_authenticated = True

        request = self.client.get('/profiles_developer/')
        request.user = MockUser()
        response = profiles_developer(request)
        self.assertContains(response, 'Logout')

    def test_profiles_developer_url_returns_correct_html(self):

        class MockUser:
            is_authenticated = True

        request = self.client.get('/profiles_developer/')
        request.user = MockUser()
        response = profiles_developer(request)
        self.assertTemplateUsed(response, 'private_profiles/profiles_developer.html', 'public_profiles/base.html')

        # When I run this case, I receive the error: 
        # ValueError: assertTemplateUsed() and assertTemplateNotUsed() are only usable on responses fetched using the Django test Client.



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