from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from public_profiles.views import home, about

class HomePageTest(TestCase):

    def test_root_url_returns_home_view(self):
        found = resolve('/')  
        self.assertEqual(found.func, home)

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'public_profiles/home.html', 'public_profiles/base.html')

class AboutPageTest(TestCase):
    
    def test_root_url_returns_about_view(self):
        found = resolve('/about/')  
        self.assertEqual(found.func, about)

    def test_about_page_returns_correct_html(self):
        response = self.client.get('/about/')
        self.assertTemplateUsed(response, 'public_profiles/about.html', 'public_profiles/base.html')



#To learn about tests I am using the book at "https://www.obeythetestinggoat.com"


# This is a test for checking the registration form - this belongs in the privite_profiles app
    # def test_can_save_a_POST_request(self):
    #     response = self.client.post('/', data={'item_text': 'A new list item'})
    #     self.assertIn('A new list item', response.content.decode())