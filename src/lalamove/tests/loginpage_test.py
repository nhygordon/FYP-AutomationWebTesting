from selenium import webdriver
import time ,sys
sys.path.append("./src/lalamove")
import unittest
from Pages.pages import LoginPage, DelviroPage
import HtmlTestRunner
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class LoginPageTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get('https://www.lalamove.com/zh-hk/')




    def test_loginlogout(self,username='95111073',password='testing8964', homename='香港沙田文林路香港文化博物館',delvironame='香港沙田文林路香港文化博物館',name2='ccc',phone2name='95111073',addressname='c'):
        driver = self.driver
        login = LoginPage(driver)
        login.click_loginpage()
        handles = driver.window_handles
        driver.switch_to.window(handles[1])
        time.sleep(5)
        login.enter_username(username)
        login.enter_Password(password)
        login.click_login()
        time.sleep(3)
        delviro = DelviroPage(driver)
        delviro.enter_home(homename)
        time.sleep(3)
        delviro.enter()
        delviro.enter_name2(name2)
        delviro.enter_phone2(phone2name)
        delviro.enter_address(addressname)
        delviro.click_save()
        time.sleep(3)
        delviro.enter_delviro(delvironame)
        if homename == delvironame:
         raise ValueError("Error: homename and delvironame are the same")
        time.sleep(3)
        delviro.enter()
        time.sleep(3)
        delviro.enteragain_delviro()
        time.sleep(3)
        delviro.enter_name2(name2)
        delviro.enter_phone2(phone2name)
        delviro.enter_address(addressname)
        delviro.click_save()
        time.sleep(3)
        delviro.click_car()
        time.sleep(5)
        delviro.click_next()
   

    @classmethod
    def tearDown(cls):
        cls.driver.quit()
        print('Test completed')

if __name__ == "__main__":
    unittest.main(verbosity=2,testRunner=HtmlTestRunner.HTMLTestRunner(output='src/lalamove/Reports'))