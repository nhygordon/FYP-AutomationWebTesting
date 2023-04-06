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
    name2_inputbox = (By.CSS_SELECTOR, "body > div.Popover.Popover-right.Popover__StyledPopover-sc-xczulu-0.kcNpHI > div > div > form > div:nth-child(1) > div > input")
    phone2_inputbox = (By.CSS_SELECTOR, "body > div.Popover.Popover-right.Popover__StyledPopover-sc-xczulu-0.kcNpHI > div > div > form > div:nth-child(2) > div > input")
    address_inputbox = (By.CSS_SELECTOR, "body > div.Popover.Popover-right.Popover__StyledPopover-sc-xczulu-0.kcNpHI > div > div > form > div:nth-child(3) > div > input")
    car_button = (By.XPATH, "//*[@id='🚐']/div[1]/div/div[2]/main/div[2]/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div[2]")
    delviro_button = (By.CSS_SELECTOR, "#🚐 > div:nth-child(1) > div > div.styles__Container-sc-vatx7q-0.kRMjGM > main > div.PlaceOrderFooter__Container-sc-1wple4i-0.jOmfob > div.PlaceOrderFooter__ButtonGroup-sc-1wple4i-4.cbnoxK")
    save_button = (By.CSS_SELECTOR, "body > div.Popover.Popover-right.Popover__StyledPopover-sc-xczulu-0.kcNpHI > div > div > form > div.Form__FormActionContainer-sc-pnea3c-3.kVVIWj > button.style__Base-sc-vh04nt-0.Button__StyledButton-sc-1gmuxjw-3.iETTwv.ccbMmc")
    enter2_home_button = (By.CSS_SELECTOR, "#🚐 > div:nth-child(1) > div > div.style__HeaderContainer-sc-1yrhzab-0.jXjUQS > div > div > div > a")
    
    