from django.test import TestCase
from django.urls import resolve
from lists.views import home_page

class SmokeTest(TestCase):
    '''test hom page'''
    
    def test_root_url_resolves_to_home_page_views(self):
        '''test: root url resolves to views home page'''
        found = resolve('/')
        self.assertEqual(found.func, home_page)
