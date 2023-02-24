from selenium import webdriver
import time ,sys
sys.path.append("./src/KFC")
import unittest
from pages.Pages import LoginPage , ProfilePage
import HtmlTestRunner



class LoginPageTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get('https://www.kfchk.com/index.html')


    def test_loginlogout_phonenumber(self):
        driver = self.driver

        login = LoginPage(driver)
        driver.implicitly_wait(1)
        login.do_screenshot("loginpage_staging")
        login.go_loginpage()
        
        login.enter_PhoneNumber()
        login.enter_Password()
        login.click_login()

        #driver.implicitly_wait(2)
        #time.sleep(2)
        driver.save_screenshot("loginpage_production")
        self.assertTrue(login.is_logined(), "didn't login.")
        
        logout = ProfilePage(driver)
        logout.go_settingpage()
        logout.go_profilepage()
        logout.click_logout()

    def test_loginpage_ui(self):
        loginpage = LoginPage(self.driver)
        loginpage.do_visual_compare("loginpage_staging","loginpage_production")
        loginpage.get_visual_compare_result("loginpage_production")

    @classmethod
    def tearDown(cls):
        cls.driver.quit()
        print('Test completed')

if __name__ == "__main__":
    unittest.main(verbosity=2,testRunner=HtmlTestRunner.HTMLTestRunner(output='src/KFC/Reports'))