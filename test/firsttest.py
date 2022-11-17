# Python program to demonstrate
# selenium

# import webdriver
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

try:
# create webdriver object
    driver = webdriver.Chrome()
# get google.co.hk
    driver.get("https://google.hk")
    m = driver.find_element("xpath","/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
#enter search text
    m.send_keys("Tutorialspoint")
#perform Google search with Keys.ENTER
    m.send_keys(Keys.RETURN)
    time.sleep(5)
    driver.close()
except Exception as e:
    print('Failed to do something: ' + str(e))