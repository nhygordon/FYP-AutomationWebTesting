from behave import *
from selenium import webdriver
import time ,sys
sys.path.append("./src/OrangeHRM")
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@given('I launch Chrome browser and login to orangeHRM')
def step_impl(context):
    context.execute_steps("""
        Given I launch Chrome browser
        When I open orange HRM homepage
        And Enter username "admin" and password "admin123"
        And Click on login button
    """)

@when('go to pim page')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#app > div.oxd-layout > div.oxd-layout-navigation > aside > nav > div.oxd-sidepanel-body > ul > li:nth-child(2) > a > span"))).click()

@when('click add')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div.orangehrm-paper-container > div.orangehrm-header-container > button"))).click()


@when('Enter First_name "{firstname}" and middle_name "{middlename}" and last_name "{lastname}" and employee_id "{id}"')
def step_impl(context,firstname,middlename,lastname,id):
    WebDriverWait(context.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div.orangehrm-employee-container > div.orangehrm-employee-form > div:nth-child(1) > div.oxd-grid-1.orangehrm-full-width-grid > div > div > div.--name-grouped-field > div:nth-child(1) > div:nth-child(2) > input"))).send_keys(firstname)
    WebDriverWait(context.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div.orangehrm-employee-container > div.orangehrm-employee-form > div:nth-child(1) > div.oxd-grid-1.orangehrm-full-width-grid > div > div > div.--name-grouped-field > div:nth-child(2) > div:nth-child(2) > input"))).send_keys(middlename)
    WebDriverWait(context.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div.orangehrm-employee-container > div.orangehrm-employee-form > div:nth-child(1) > div.oxd-grid-1.orangehrm-full-width-grid > div > div > div.--name-grouped-field > div:nth-child(3) > div:nth-child(2) > input"))).send_keys(lastname)
    #WebDriverWait(context.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div.orangehrm-employee-container > div.orangehrm-employee-form > div:nth-child(1) > div.oxd-grid-2.orangehrm-full-width-grid > div > div > div:nth-child(2) > input"))).clear().send_keys(id)

@then(u'click save')
def step_impl(context):
    WebDriverWait(context.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div.oxd-form-actions > button.oxd-button.oxd-button--medium.oxd-button--secondary.orangehrm-left-space"))).click()
