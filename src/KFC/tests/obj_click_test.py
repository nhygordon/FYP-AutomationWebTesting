from distutils.log import error
import time
import click
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os ,sys
sys.path.append("./src/KFC")
import unittest
from pages.Pages import BasePage2
import HtmlTestRunner

class OrderTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get('https://www.kfchk.com/index.html')

    def test_obj_click(self):
        driver = self.driver

        click = BasePage2(driver)
        click.close_frame()
        click.scroll_to_buttom()
        time.sleep(2)
        click.click_test()

        

    @classmethod
    def tearDown(cls):
        cls.driver.quit()
        
        print('Test completed')

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HtmlTestRunner.HTMLTestRunner(output='src/KFC/Reports'))