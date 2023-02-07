from selenium import webdriver
import os ,sys
sys.path.append("./src/KFC")
import unittest
from pages.Pages import LoginPage , ProfilePage
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


    def test_loginlogout_phonenumber(self):
        driver = self.driver

        login = LoginPage(driver)
        driver.implicitly_wait(1)
        #time.sleep(1)
        login.do_screenshot("loginpage_staging")
        login.go_loginpage()
        
        login.enter_PhoneNumber(user_phonenumber)
        login.enter_Password(user_password)
        login.click_login()
        driver.implicitly_wait(2)
        #time.sleep(1)
        driver.save_screenshot("loginpage_production")
        self.assertTrue(login.is_logined(), "didn't login.")
        
        '''
        #main page to login page
        WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.ID,"frame1")))
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.login"))).click()
        
        #login
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[4]/div/div[1]/input"))).send_keys(user_phonenumber)
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[4]/div/div[2]/input"))).send_keys(user_password)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.loginBtn"))).click()
        time.sleep(5)
        '''
        logout = ProfilePage(driver)
        logout.go_profilepage()
        logout.click_logout()

        
        '''
        #logout
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.mine"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span.cellName"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.btn"))).click()
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[5]/div/div[2]/span[2]"))).click()
        '''

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