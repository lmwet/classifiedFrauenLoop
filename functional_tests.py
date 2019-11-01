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
        # Ms X found out about Frauenloop classified and wants to check it out
        self.browser.get('http://localhost:8000')
        self.assertIn('Frauenloop', self.browser.title)  
        self.fail('Finish the test!')

        # Ms X thinks it's a super cool idea and decides she must set up an account immediately
        # She goes to the register page and fills in her details
        # She clicks submit and the page returns her to the login page
        # She's so excited she decides to complete her profile straight away so she logs in
        # Ms X navigates to her profile page and completes her profile.
        # She saves the information and logs out because she has an important appointment in 5 minutes
        # Later she comes back and wants to edit her bio, so she logs back in
        # She edits her bio then goes to bed


    if __name__ == '__main__':  
        unittest.main(warnings='ignore')  