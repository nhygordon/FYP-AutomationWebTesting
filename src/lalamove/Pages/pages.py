import sys , os
sys.path.append("./src/lalamove")
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Locators.locators import LoginPageLocators, MainpageLocators, LocationPageLocators
from skimage.metrics import structural_similarity
import imutils
import cv2
from PIL import Image
import time

class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""
    def __init__(self, driver):
        self.driver = driver

        

    def do_screenshot(self, file_name):
        self.driver.save_screenshot("./Screenshot/{}.png".format(file_name))
    
    def get_visual_compare_result(self,filename):
        #read the image, creating an object
        im = Image.open(r"./src/lalamove/Reports/images/{}.png".format(filename))
        #show picture
        print(im.show())
    
    def do_visual_compare(self,image_staging,image_production):
        imageA = cv2.imread("./src/lalamove/Screenshot/{}.png".format(image_staging))
        imageB = cv2.imread("./src/lalamove/Screenshot/{}.png".format(image_production))
        
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
        cv2.imwrite("./src/lalamove/Reports/screenshot_result/{}.png".format(image_staging),imageA)
        # cv2.imshow("Modified", imageB)
        cv2.imwrite("./src/lalamove/Reports/screenshot_result/{}.png".format(image_production),imageB)
        # cv2.imshow("Diff", diff)
        cv2.waitKey(0)

class LoginPage(BasePage):

    def click_loginpage(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(MainpageLocators.dashboard_button)).click()
        
    def enter_username(self,username= '95111073'):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LoginPageLocators.user_inputbox)).click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LoginPageLocators.user_inputbox)).send_keys(username)

    def enter_Password(self,password='iamgayhehe'):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LoginPageLocators.password_inputbox)).click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LoginPageLocators.password_inputbox)).send_keys(password)
    
    def click_login(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(LoginPageLocators.login_button)).click()


class Contents(BasePage):
    
    def go_dashboard(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(MainpageLocators.dashboard_button)).click()

class DelviroPage(BasePage):
    def enter_home(self,homename='香港沙田文林路香港文化博物館'):
        home_input_box = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocationPageLocators.home_inputbox))
        home_input_box.click()
        home_input_box.send_keys(homename)

    def enter(self):
        home_input_box = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocationPageLocators.home_inputbox))
        home_input_box.send_keys(Keys.ENTER)

    def enter2_home(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocationPageLocators.enter2_home_button)).click()

    def click_car(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocationPageLocators.car_button)).click()
        

    def enter_delviro(self,delvironame='香港沙田文林路香港文化博物館'):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocationPageLocators.devliro_inputbox)).click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocationPageLocators.devliro_inputbox)).send_keys(delvironame)
    
    def enteragain_delviro(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocationPageLocators.devliro_inputbox)).click()
    
    def enter_name2(self,name2='ccc'):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocationPageLocators.name2_inputbox)).click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocationPageLocators.name2_inputbox)).send_keys(name2)

    def enter_phone2(self,phone2name='95111073'):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocationPageLocators.phone2_inputbox)).click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocationPageLocators.phone2_inputbox)).send_keys(phone2name)

    def enter_address(self,addressname='c'):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocationPageLocators.address_inputbox)).click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LocationPageLocators.address_inputbox)).send_keys(addressname)

    def click_next(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(LocationPageLocators.delviro_button)).click()

    def click_save(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(LocationPageLocators.save_button)).click()
    



    

class Dashboard():
    pass
