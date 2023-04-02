from selenium.webdriver.common.by import By
class MainpageLocators(object):
    dashboard_button = (By.CSS_SELECTOR, "#hs_cos_wrapper_header_login_btn > a")
    
class LoginPageLocators(MainpageLocators):
    user_inputbox = (By.CSS_SELECTOR, "#🚐 > div:nth-child(1) > div > div.Container-sc-1y5phmm-1.khwpCj > div > form > div:nth-child(1) > div > div > div")
    password_inputbox = (By.CSS_SELECTOR, "#🚐 > div:nth-child(1) > div > div.Container-sc-1y5phmm-1.khwpCj > div > form > div:nth-child(2) > div")
    login_button = (By.CSS_SELECTOR, "#🚐 > div:nth-child(1) > div > div.Container-sc-1y5phmm-1.khwpCj > div > form > button")

class LocationPageLocators(MainpageLocators):
    home_inputbox = (By.CSS_SELECTOR, "#🚐 > div:nth-child(1) > div > div.styles__Container-sc-vatx7q-0.kRMjGM.appear-done.enter-done > main > div.styles__LeftContent-sc-vatx7q-2.bwzRZK > div > div.PlaceOrder__AnimationWrapper-sc-1e843if-3.EmrNP > div > div:nth-child(1) > div > ul > li:nth-child(1) > div > div > div")
    devliro_inputbox = (By.CSS_SELECTOR, "#🚐 > div:nth-child(1) > div > div.Container-sc-1y5phmm-1.khwpCj > div > form > div:nth-child(1) > div")
    delviro_button = (By.CSS_SELECTOR, "#🚐 > div:nth-child(1) > div > div.Container-sc-1y5phmm-1.khwpCj > div > form > div:nth-child(2) > div > div > label")