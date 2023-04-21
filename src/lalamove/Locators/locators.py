from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class MainpageLocators(object):
    dashboard_button = (By.CSS_SELECTOR, "#hs_cos_wrapper_header_login_btn > a")
    
class LoginPageLocators(MainpageLocators):
    user_inputbox = (By.CSS_SELECTOR, "#username")
    password_inputbox = (By.CSS_SELECTOR, "#password")
    login_button = (By.XPATH, "//*[@id='🚐']/div[1]/div/div[1]/div/form/button")

class LocationPageLocators(MainpageLocators):
    home_inputbox = (By.CSS_SELECTOR, "#downshift-3-input")
    devliro_inputbox = (By.CSS_SELECTOR, "#downshift-4-input")
    name2_inputbox = (By.CSS_SELECTOR, "body > div.Popover.Popover-right.css-wamzlp.etss4940 > div > div > form > div:nth-child(1) > div > input")
    phone2_inputbox = (By.CSS_SELECTOR, "body > div.Popover.Popover-right.css-wamzlp.etss4940 > div > div > form > div:nth-child(2) > div > input")
    address_inputbox = (By.CSS_SELECTOR, "body > div.Popover.Popover-right.css-wamzlp.etss4940 > div > div > form > div:nth-child(3) > div > input")
    car_button = (By.XPATH, "//*[@id='🚐']/div[1]/div/div[2]/main/div[2]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div[2]")
    delviro_button = (By.CSS_SELECTOR, "#🚐 > div:nth-child(1) > div > div.css-125p82w.e5yta295 > main > div.css-cale47.ewx3rcp2 > div.css-udmynv.ewx3rcp1 > button")
    save_button = (By.CSS_SELECTOR, "body > div.Popover.Popover-right.css-wamzlp.etss4940 > div > div > form > div.css-1szkkvs.exwk2gb0 > button.css-q4k3ze.ehazdfk0")
    enter2_home_button = (By.CSS_SELECTOR, "#🚐 > div:nth-child(1) > div > div.style__HeaderContainer-sc-1yrhzab-0.jXjUQS > div > div > div > a")
    
    