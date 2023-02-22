from selenium import webdriver
import time ,sys
sys.path.append("./src/OrangeHRM")
import unittest
from Pages.pages import LoginPage
import HtmlTestRunner
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class LoginPageTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    def test_loginlogout(self,username='Admin',password='admin123'):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_username()
        login.enter_Password()
        login.click_login()
   

    @classmethod
    def tearDown(cls):
        cls.driver.quit()
        print('Test completed')

if __name__ == "__main__":
    unittest.main(verbosity=2,testRunner=HtmlTestRunner.HTMLTestRunner(output='src/OrangeHRM/Reports'))