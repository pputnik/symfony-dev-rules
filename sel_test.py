# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Py(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://yp.org.ua/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_py(self):
        driver = self.driver
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | null | ]]
        driver.get(self.base_url + "/perl/")
        self.assertTrue(self.is_element_present(By.LINK_TEXT, "Learning Perl"))
        driver.find_element_by_link_text("Learning Perl").click()
        self.assertEqual("Chapter 2: Scalar Data", driver.find_element_by_link_text("Chapter 2: Scalar Data").text)
        driver.find_element_by_link_text("Chapter 2: Scalar Data").click()
#        self.assertRegexpMatches(driver.find_element_by_link_text("2.1 What Is Scalar Data?").text, r"^exact:2\.1 What Is Scalar Data[\s\S]$")
        driver.find_element_by_link_text("<STDIN> as a Scalar Value").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

#http://www.qaclubkiev.com/2013/01/how-to-start-with-selenium-c-java-python.html
#http://docs.seleniumhq.org/docs/03_webdriver.jsp#selenium-webdriver-api-commands-and-operations
#https://selenium-python.readthedocs.org/getting-started.html
