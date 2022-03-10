from selenium import webdriver
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
        self.fail('done test!')
        #ей сразу же предлагается ввести элемент списка.

        #Она набирает в тектовом поле "купить павлиньи перья"
        #(ее хобби - вязание рыболовных мушек)

        #когда она нажимает enter, страница обновляется, и теперь страница
        #содержит "1: Купить павлиньи перья" в качестве элемента списка

        #текстовое поле по-прежнему приглашает ее добавить еще один элемент.
        #она вводит "сделать мушку из павлиньих перьев"
        #(Эдит очень методична)

        #Страница снова обновляется, и теперь показывает оба элемента ее списка

        #Эдит интересно, запомнит ли сайт ее список. Далее она видит, что сайт
        #сгенерировал для нее уникальный URL-адресс - об этом
        #выводится небольшой текст с объяснениями.

        #Она посещает этот URL-адресс - ее список по прежнему там.

        #Удовлетворенная, она снова ложится спать


if __name__ == '__main__':
    unittest.main(warnings='ignore')
