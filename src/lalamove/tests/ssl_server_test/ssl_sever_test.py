import time
from selenium import webdriver
import os ,sys
sys.path.append("./src/lalamove")
import unittest
import HtmlTestRunner
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

path = 'https://www.lalamove.com/zh-hk/'
textbox = (By.CSS_SELECTOR,"#main > div.submitBox > center > form > table > tbody > tr:nth-child(1) > td:nth-child(2) > input[type=text]")
submit = (By.CSS_SELECTOR, "#main > div.submitBox > center > form > table > tbody > tr:nth-child(1) > td:nth-child(3) > input[type=submit]")
summary = (By.CSS_SELECTOR, "#main > div:nth-child(6) > div:nth-child(1) > div.sectionTitle")

class ProfilePageTest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(chrome_options=chrome_options)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        cls.driver.get('https://www.ssllabs.com/ssltest/index.html')        
    
    @classmethod 
    def test_ssl_server(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(textbox)).send_keys(path)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(submit)).click()
        WebDriverWait(self.driver, 500).until(EC.visibility_of_element_located(summary))


    @classmethod
    def tearDown(cls):
        print('Testing had already run on the external website.')
        
if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='src/lalamove/Reports'))