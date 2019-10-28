from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_frauenlooper_can_access_classified(self):
        #Ms X found out about Frauenloop classified and wants to check it out
        self.browser.get('http://localhost:8000')


        #This does not react when I run this on cmd - why??