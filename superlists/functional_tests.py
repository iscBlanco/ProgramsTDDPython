from selenium import webdriver
import unittests

class NewVisitorTest(unittest.TestCase):	#1

    def setUp(self):	#2
        self.browser = webdriver.Firefox()
    
    def tearDown(self):    #3
    	self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):    #4
        # Edith has heard about a cool new online to-do app. She goes
        # to checkout its homepage
