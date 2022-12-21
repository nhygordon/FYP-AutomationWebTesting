from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import unittest

# login_info
user_pn = os.getenv('KFC_PN')
user_pw = os.getenv('KFC_PW')

class LogInLogOutTest(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get('https://www.kfchk.com/index.html')

    def test_loginlogout_valid(self):
        driver = self.driver
        #main page to login page
        WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.ID,"frame1")))
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.login"))).click()
        #login
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[4]/div/div[1]/input"))).send_keys(user_pn)
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[4]/div/div[2]/input"))).send_keys(user_pw)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.loginBtn"))).click()
        time.sleep(5)
        #logout
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.mine"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span.cellName"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.btn"))).click()
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[5]/div/div[2]/span[2]"))).click()

    @classmethod
    def tearDown(cls):
        cls.driver.quit()
        print('Test completed')

if __name__ == "__main__":
    unittest.main()