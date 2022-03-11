from django.test import TestCase

class SmokeTest(TestCase):
    '''test for toxic'''
    
    def test_bad_maths(self):
        '''test: wrong math comp'''
        
        self.assertEqual(1 + 1, 3)
