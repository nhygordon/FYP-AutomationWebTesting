from distutils.log import error
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os ,sys
sys.path.append("./src/KFC")
import unittest
from pages.Pages import SelectShopPage, SelectFoodPage
import HtmlTestRunner

class OrderTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get('https://www.kfchk.com/index.html')

    def test_order_valid(self):
        driver = self.driver

        order = SelectShopPage(driver)
        order.go_takeoutpage()
        order.click_shop()
        
        select = SelectFoodPage(driver)
  
        for i in range(30):
            select.choose_original()
            select.order_original()

    @classmethod
    def tearDown(cls):
        cls.driver.quit()
        
        print('Test completed')

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=HtmlTestRunner.HTMLTestRunner(output='src/KFC/Reports'))