from selenium import webdriver
import os ,sys
sys.path.append("./src/KFC")
import unittest
from pages.Pages import LoginPage 
import HtmlTestRunner
# login_info
user_phonenumber = os.getenv('KFC_PN')
user_password = os.getenv('KFC_PW')
# print(user_password)

class LoginPageTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get('https://www.kfchk.com/index.html')

       
    def test_loginpage_ui(self):
        loginpage = LoginPage(self.driver)
        loginpage.do_visual_compare("loginpage_staging","loginpage_production")
        loginpage.get_visual_compare_result("loginpage_production")

    @classmethod
    def tearDown(cls):
        cls.driver.quit()
        print('Test completed')


if __name__ == "__main__":
    unittest.main(verbosity=2,testRunner=HtmlTestRunner.HTMLTestRunner(output='src/KFC/Reports',report_title='loginpage ui test',))