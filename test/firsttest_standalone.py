# Python program to demonstrate
# selenium

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
class googlesearch(unittest.TestCase):
    def setUp(self):
        # create webdriver object
        from selenium import webdriver

        self.driver = webdriver.Remote(
        command_executor='http://192.168.56.1:4444/wd/hub',
        options=webdriver.ChromeOptions()
        )

        #self.driver = webdriver.Chrome()
        # get google.co.hk
        self.driver.get("https://google.hk")

    def test_google_search(self):
        driver = self.driver
        m = driver.find_element("xpath","/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
        print(m)
#enter search text
        m.send_keys("Tutorialspoint")
#perform Google search with Keys.ENTER
        m.send_keys(Keys.RETURN)
        self.assertIn("Tutorialspoint", driver.title)
        self.assertNotIn("No results found.", driver.page_source)
        

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()