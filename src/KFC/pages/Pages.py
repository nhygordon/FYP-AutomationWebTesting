import sys
sys.path.append("./src/KFC")
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.locators import MainpageLocators, LoginPageLocators , ProfilePageLocators

class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""
    def __init__(self, driver):
        self.driver = driver
    
    def go_loginpage(self):
        WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it( MainpageLocators.app_frame))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(MainpageLocators.loginpage_button)).click()
    
    def go_settingpage(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(MainpageLocators.settingpage_button)).click()
    
    def go_profilepage(self):
        self.go_settingpage()    
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(MainpageLocators.profilepage_button)).click()

class LoginPage(BasePage):
    '''
    def __init__(self):
        self.PhoneNumber_textbox_xpath = "//*[@id='app']/div[1]/div[4]/div/div[1]/input"
        self.password_textbox_xpath = "//*[@id='app']/div[1]/div[4]/div/div[2]/input"
        self.login_button_css_selector = "div.loginBtn"
    '''
    def enter_PhoneNumber(self, phonenumber):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LoginPageLocators.phonenumber_inputbox)).clear()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LoginPageLocators.phonenumber_inputbox)).send_keys(phonenumber)

    def enter_Password(self, password):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LoginPageLocators.password_inputbox)).clear()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LoginPageLocators.password_inputbox)).send_keys(password)
    
    def click_login(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(LoginPageLocators.login_button)).click()

class ProfilePage(BasePage):
    '''
    def __init__(self):
        self.logout_button_css_selector = "div.btn"
        self.logout_confirm_xpath = "//*[@id='app']/div[1]/div[5]/div/div[2]/span[2]"
    '''
    def click_logout(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(ProfilePageLocators.logout_button)).click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(ProfilePageLocators.logout_confirm_button)).click()