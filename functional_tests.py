from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    '''test new incomer'''
    
    def setUp(self):
        '''install'''
        self.browser    = webdriver.Firefox()
    
    def tearDown(self):
        '''uninstall'''
        self.browser.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        '''тест: можно начать список и получить его позже'''
        #Edit listen about new cool online-app for to do list
        #she should rate this home page.
        self.browser.get('http://localhost:8000')
        #she see, that header and cap-page says about TDL.

        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        #ей сразу же предлагается ввести элемент списка.
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item')
        #Она набирает в тектовом поле "купить павлиньи перья"
        #(ее хобби - вязание рыболовных мушек)
        inputbox.send_keys('buy pavlins perya')
        
        #когда она нажимает enter, страница обновляется, и теперь страница
        #содержит "1: Купить павлиньи перья" в качестве элемента списка
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(
            '1: buy pavlins perya',[row.text for row in rows])
            #f"new element lists don't show in table.\ncontent is:\n{table.text}")
        #текстовое поле по-прежнему приглашает ее добавить еще один элемент.
        #она вводит "сделать мушку из павлиньих перьев"
        #(Эдит очень методична)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('make peacock')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        
        #Страница снова обновляется, и теперь показывает оба элемента ее списка
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: buy pavlins perya', [row.text for row in rows])
        self.assertIn(
            '2: make peacock',
            [row.text for row in rows])
        #Эдит интересно, запомнит ли сайт ее список. Далее она видит, что сайт
        #сгенерировал для нее уникальный URL-адресс - об этом
        #выводится небольшой текст с объяснениями.
        self.fail('done test!')

        #Она посещает этот URL-адресс - ее список по прежнему там.

        #Удовлетворенная, она снова ложится спать


if __name__ == '__main__':
    unittest.main(warnings='ignore')
