from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time

MAX_WAIT = 3


class NewVisitorTest(LiveServerTestCase):
    '''test new incomer'''
    
    def setUp(self):
        '''install'''
        self.browser    = webdriver.Firefox()
    
    def tearDown(self):
        '''uninstall'''
        self.browser.quit()
    
    def wait_for_row_in_list_table(self, row_text):
        '''assert for str in list table'''
        
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
            
    
    def test_can_start_a_list_for_one_user(self):
        '''тест: можно начать список и получить его позже'''
        #Edit listen about new cool online-app for to do list
        #she should rate this home page.
        self.browser.get(self.live_server_url)
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
        #time.sleep(1)
        self.wait_for_row_in_list_table('1: buy pavlins perya')
        
        #текстовое поле по-прежнему приглашает ее добавить еще один элемент.
        #она вводит "сделать мушку из павлиньих перьев"
        #(Эдит очень методична)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('make peacock')
        inputbox.send_keys(Keys.ENTER)
        #time.sleep(1)
        
        #Страница снова обновляется, и теперь показывает оба элемента ее списка
        self.wait_for_row_in_list_table('2: make peacock')
        self.wait_for_row_in_list_table('1: buy pavlins perya')
        #Эдит интересно, запомнит ли сайт ее список. Далее она видит, что сайт
        #сгенерировал для нее уникальный URL-адресс - об этом
        #выводится небольшой текст с объяснениями.
        #self.fail('done test!')

        #Она посещает этот URL-адресс - ее список по прежнему там.

        #Удовлетворенная, она снова ложится спать
    
    def test_multiple_users_can_start_lists_at_different_urls(self):
        '''test: multi users can start lists at dif urls'''
        
        #Edit start a new list
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('buy pavlins perya')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: buy pavlins perya')
        
        #she see, what her list has uniq url-adress
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')
        
        #now the new user, Francis come to site
        
        #we use a new seanse of browser
        self.browser.quit()
        self.browser = webdriver.Firefox()
        
        #Francis go to home page
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('byu pavlins perya', page_text)
        self.assertNotIn('make peacock', page_text)
        
        #Francis start a new list
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('buy milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: buy milk')
        
        #Francis take a uniq url-adress
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)
        
        #not have any from Edith
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('byu pavlins perya', page_text)
        self.assertIn('buy milk', page_text)
        
        #go to sleep


if __name__ == '__main__':
    unittest.main(warnings='ignore')
