from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from lists.views import home_page

class HomePageTest(TestCase):
    '''test home page'''
    
    def test_root_url_resolves_to_home_page_views(self):
        '''test: root url resolves to views home page'''
        found = resolve('/')
        self.assertEqual(found.func, home_page)
    
    def test_home_page_returns_correct_html(self):
        '''test: home page returns correct html'''
        request     = HttpRequest()
        response    = home_page(request)
        html    = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))
