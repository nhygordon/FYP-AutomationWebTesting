from selenium import webdriver
import os ,sys
sys.path.append("./src/KFC")
import unittest
from pages.Pages import ProfilePage
import HtmlTestRunner
from ddt import ddt,data,unpack
import time

@ddt
class ProfilePageTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get('https://www.kfchk.com/index.html')
        # login in frist to do further action
        login = ProfilePage(cls.driver)
        login.go_loginpage()
        login.enter_PhoneNumber()
        login.enter_Password()
        login.click_login()
        login.go_settingpage()
        login.go_profilepage()

    def test_modify_username(self):
        driver = self.driver
        profile_name = ProfilePage(driver)
        profile_name.modify_username('testing')

    @data(['M','男'],['F','女'],['ND','非公開'])
    @unpack
    def test_modify_gender(self,gender,suppose_vaiable):
        profile_gender = ProfilePage(self.driver)
        profile_gender.modify_gender(gender)
        profile_gender.left()
        profile_gender.go_profilepage()
        time.sleep(2)
        current_variable = profile_gender.get_currnet_gender()
        print(profile_gender.get_currnet_gender())
        print(current_variable)
        self.assertEqual(suppose_vaiable,current_variable)


    @classmethod
    def tearDown(cls):
        cls.driver.quit()
        print('Test completed')

if __name__ == "__main__":
    unittest.main(verbosity=2,testRunner=HtmlTestRunner.HTMLTestRunner(output='src/KFC/Reports'))