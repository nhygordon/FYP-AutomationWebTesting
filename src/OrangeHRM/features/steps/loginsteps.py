from behave import *
from selenium import webdriver
import time ,sys
sys.path.append("./src/OrangeHRM")
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@given('I launch Chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()

@when('I open orange HRM homepage')
def step_impl(context):
    context.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

@when('Enter username "{username}" and password "{password}"')
def step_impl(context,username,password):
    WebDriverWait(context.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > form > div:nth-child(2) > div > div:nth-child(2) > input"))).send_keys(username)
    WebDriverWait(context.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > form > div:nth-child(3) > div > div:nth-child(2) > input"))).send_keys(password)
@when('Click on login button')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > form > div.oxd-form-actions.orangehrm-login-action > button"))).click()

@then('User must successfully login to the Dashboard page')
def step_impl(context):
    try:
        text = WebDriverWait(context.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(8) > a > span"))).text
    except:
        context.driver.close()
        assert False ,"Test Failed"
    if text =="Dashboard":
        context.driver.close()
        assert True , "Test Passed"