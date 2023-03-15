from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('launch chrome browser')
def LaunchBrowser(context):
   context.driver = webdriver.Chrome()


@when('open orange hrm homepage')
def OpenHomePage(context):
   context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


@then('verify that the logo present on Page')
def VeriflyLogo(context):
   status = context.driver.find_element(By.CSS_SELECTOR, '#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-branding > img').is_displayed()
   assert status is True
   
@then('close browser')
def closeBrowser(context):
   context.driver.quit()