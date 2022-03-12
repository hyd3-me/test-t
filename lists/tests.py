from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from lists.views import home_page

class HomePageTest(TestCase):
    '''test home page'''
    
    def test_uses_home_page_template(self):
        '''test: uses home templates'''
        
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
