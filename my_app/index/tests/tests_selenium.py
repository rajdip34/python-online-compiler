"""
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class AccountTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', port=9515)
        self.selenium.get('http://www.google.com/xhtml');
        time.sleep(5)  # Let the user actually see something!
        super(AccountTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(AccountTestCase, self).tearDown()

    def test_register(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('http://127.0.0.1:8000/login/')
        #find the form element
        username = selenium.find_element_by_id('username')
        password1 = selenium.find_element_by_id('password')
        submit = selenium.find_element_by_name('loginsubmit')
        #Fill the form with data
        username.send_keys('unary')
        password1.send_keys('123456')
        #submitting the form
        submit.send_keys(Keys.RETURN)

        #check the returned result
        assert 'Check your email' in selenium.page_source
"""