#import KFC.Locators 
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""
    def __init__(self, driver):
        self.driver = driver
        self.app_frame_id = "frame1"
        self.loginpage_button_css_selector = "div.login"
        

    def go_loginpage(self):
        WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.ID, self.app_frame_id)))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.loginpage_button_css_selector))).click()
    
    def go_settingpage(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.mine"))).click()
    
    def go_profilepage(self):
        self.go_settingpage()    
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span.cellName"))).click()

class LoginPage(BasePage):
    '''
    def __init__(self):
        self.PhoneNumber_textbox_xpath = "//*[@id='app']/div[1]/div[4]/div/div[1]/input"
        self.password_textbox_xpath = "//*[@id='app']/div[1]/div[4]/div/div[2]/input"
        self.login_button_css_selector = "div.loginBtn"
    '''
    def enter_PhoneNumber(self, phonenumber):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[4]/div/div[1]/input"))).clear()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[4]/div/div[1]/input"))).send_keys(phonenumber)

    def enter_Password(self, password):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[4]/div/div[2]/input"))).clear()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[4]/div/div[2]/input"))).send_keys(password)
    
    def click_login(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.loginBtn"))).click()

class AccountSettingPage(BasePage):
    '''
    def __init__(self):
        self.logout_button_css_selector = "div.btn"
        self.logout_confirm_xpath = "//*[@id='app']/div[1]/div[5]/div/div[2]/span[2]"
    '''
    def click_logout(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div.btn"))).click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='app']/div[1]/div[5]/div/div[2]/span[2]"))).click()