from selenium.webdriver.common.by import By
class MainpageLocators(object):
    app_frame = (By.ID, "frame1")
    loginpage_button = (By.CSS_SELECTOR, "div.login")
    settingpage_button = (By.CSS_SELECTOR, "div.mine")
    profilepage_button = (By.CSS_SELECTOR, "span.cellName")


class LoginPageLocators(MainpageLocators):
    phonenumber_inputbox = (By.XPATH, "//*[@id='app']/div[1]/div[4]/div/div[1]/input")
    password_inputbox = (By.XPATH, "//*[@id='app']/div[1]/div[4]/div/div[2]/input")
    login_button = (By.CSS_SELECTOR, "div.loginBtn")


class ProfilePageLocators(MainpageLocators):
    logout_button = (By.CSS_SELECTOR, "div.btn")
    logout_confirm_button = (By.XPATH, "//*[@id='app']/div[1]/div[5]/div/div[2]/span[2]")