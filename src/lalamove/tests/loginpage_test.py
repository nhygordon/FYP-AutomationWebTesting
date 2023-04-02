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
        cls.driver.get('https://www.lalamove.com/zh-hk/')
        cls.driver2 = webdriver.Chrome()
        cls.driver2.implicitly_wait(10)
        cls.driver2.maximize_window()
        cls.driver2.implicitly_wait(10)
        cls.driver2.get('https://web.lalamove.com/login?_branch_match_id=827113453468420606&_branch_referrer=H4sIAAAAAAAAA8soKSkottLXz0nMSczNL0vVSywo0MvJzMvWryqKLDYqcEz1SUsCAFOoooElAAAA')



    def test_loginlogout(self,username='95111073',password='iamgayhehe', home='宏照道九龍灣香港',delviro='宏照道九龍灣香港'):
        driver = self.driver
        login = LoginPage(driver)
        login.enter_username(username)
        login.enter_Password(password)
        login.click_login()
        delviro = DelviroPage(driver)
        delviro.enter_home(home)
        delviro.enter_delviro(delviro)
        delviro.click_next()
   

    @classmethod
    def tearDown(cls):
        cls.driver2.quit()
        print('Test completed')

if __name__ == "__main__":
    unittest.main(verbosity=2,testRunner=HtmlTestRunner.HTMLTestRunner(output='src/lalamove/Reports'))