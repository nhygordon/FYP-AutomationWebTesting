#import KFC.Locators 
import os
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
<<<<<<< Updated upstream
from Locators.locators import MainpageLocators, LoginPageLocators , ProfilePageLocators, TakeOutPageLocators, OrderPageLocators, OrderPageLocators

=======
from Locators.locators import MainpageLocators, Mainpage2Locators, LoginPageLocators , ProfilePageLocators, TakeOutPageLocators, OrderPageLocators, EmailPageLocators
from skimage.metrics import structural_similarity
import imutils
import cv2
from PIL import Image
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
>>>>>>> Stashed changes


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
    
    def go_personalinfopage(self):
        self.go_settingpage()    
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span.cellName"))).click()

    def go_takeOutpage(self):
        WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.ID, self.app_frame_id)))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(MainpageLocators.take_out_button)).click()
    
    def do_screenshot(self, file_name):
        self.driver.save_screenshot("./Screenshot/{}.png".format(file_name))
    
    def get_visual_compare_result(self,filename):
        #read the image, creating an object
        im = Image.open(r"./src/KFC/Reports/images/{}.png".format(filename))
        #show picture
        print(im.show())
    
    def do_visual_compare(self,image_staging,image_production):
        imageA = cv2.imread("./src/KFC/Screenshot/{}.png".format(image_staging))
        imageB = cv2.imread("./src/KFC/Screenshot/{}.png".format(image_production))
        
        # convert the images to grayscale
        grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
        grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
        (score, diff) = structural_similarity(grayA, grayB, full=True)
        diff = (diff * 255).astype("uint8")
        print("SSIM: {}".format(score))
        thresh = cv2.threshold(diff, 0, 255,
            cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        for c in cnts:
            # images differ
            (x, y, w, h) = cv2.boundingRect(c)
            cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)
        
        # show the output images
        # cv2.imshow("Original", imageA)
        cv2.imwrite("./src/KFC/Reports/screenshot_result/{}.png".format(image_staging),imageA)
        # cv2.imshow("Modified", imageB)
        cv2.imwrite("./src/KFC/Reports/screenshot_result/{}.png".format(image_production),imageB)
        # cv2.imshow("Diff", diff)
        cv2.waitKey(0)
    
    def scroll_to_buttom(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(Mainpage2Locators.body))
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    
class BasePage2(BasePage):
    def close_frame(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(Mainpage2Locators.close_button)).click()
    
    def click_test(self):
        element = self.driver.find_element(By.CSS_SELECTOR, "body > div.page-area > div.cookie-area.py-5.position-fixed.start-0.bottom-0.w-100 > div > div > div > div")
        loc = element.location
        X, Y = loc.get('x') + 1, loc.get('y')
        action = ActionChains(self.driver)
        action.move_by_offset(X,Y)

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

class PersonalInfoPage(BasePage):
    '''
    def __init__(self):
        self.logout_button_css_selector = "div.btn"
        self.logout_confirm_xpath = "//*[@id='app']/div[1]/div[5]/div/div[2]/span[2]"
    '''
    def click_logout(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(ProfilePageLocators.logout_button)).click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(ProfilePageLocators.logout_confirm_button)).click()
    
class SelectShopPage(BasePage):
    def click_shop(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(TakeOutPageLocators.selectShop_button)).click()
        
        
class SelectFoodPage(BasePage): 
    def choose_original(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(OrderPageLocators.à_la_carte_button)).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(OrderPageLocators.chooseOriginal_button)).click()

    def order_original(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(OrderPageLocators.addOriginal_button)).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(OrderPageLocators.addToCart_button)).click()

