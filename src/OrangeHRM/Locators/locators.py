from selenium.webdriver.common.by import By
class MainpageLocators(object):
    app_frame = (By.ID, "frame1")
    loginpage_button = (By.CSS_SELECTOR, "div.login")
    settingpage_button = (By.CSS_SELECTOR, "div.mine")
    profilepage_button = (By.CSS_SELECTOR, "#app > div.mine > div.cellList > div.cellBox.active > div > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > img")
    take_out_button = (By.CSS_SELECTOR, "#main > div.bodyInfo > div.order > div:nth-child(2) > img")

class LoginPageLocators(MainpageLocators):
    user_inputbox = (By.CSS_SELECTOR, "#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > form > div:nth-child(2) > div > div:nth-child(2) > input")
    password_inputbox = (By.CSS_SELECTOR, "#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > form > div:nth-child(3) > div > div:nth-child(2) > input")
    login_button = (By.CSS_SELECTOR, "#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > form > div.oxd-form-actions.orangehrm-login-action > button")
    