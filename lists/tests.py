from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from lists.views import home_page
from lists.models import Item


class HomePageTest(TestCase):
    '''test home page'''
    
    def test_uses_home_page_template(self):
        '''test: uses home templates'''
        
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
    
    def test_can_save_a_POST_request(self):
        '''test: can save post-req'''
        
        self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        '''test: redirect after POST-req'''
        
        response = self.client.post('/', data={'item_text': \
            'A new list item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/lists/uniq_list/')

    def test_only_saves_items_when_necessary(self):
        '''test: saves elems only when necessary'''
        
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)


class ItemModelTest(TestCase):
    '''test model elemetn lists'''
    
    def test_saving_and_retrieving_items(self):
        '''test saving and retieving lists element'''
        
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()
        
        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()
        
        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)
        
        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')


class ListViewTest(TestCase):
    '''test: vies list'''
    
    def test_uses_list_template(self):
        '''test: uses lists template'''
        
        response = self.client.get('/lists/uniq_list/')
        self.assertTemplateUsed(response, 'list.html')
    
    def test_displays_all_items(self):
        '''test: views all elems list'''
        
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')
        
        response = self.client.get('/lists/uniq_list/')
        
        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')
