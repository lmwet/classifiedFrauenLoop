from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from public_profiles.views import home

class HomePageTest(TestCase):

    def test_root_url_returns_home_view(self):
        found = resolve('/')  
        self.assertEqual(found.func, home)

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'public_profiles/home.html', 'public_profiles/base.html')