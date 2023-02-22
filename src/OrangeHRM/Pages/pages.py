import sys , os
sys.path.append("./src/OrangeHRM")
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Locators.locators import LoginPageLocators
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

class LoginPage(BasePage):

    def enter_username(self,username= 'Admin'):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LoginPageLocators.user_inputbox)).clear()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LoginPageLocators.user_inputbox)).send_keys(username)

    def enter_Password(self,password='admin123'):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LoginPageLocators.password_inputbox)).clear()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LoginPageLocators.password_inputbox)).send_keys(password)
    
    def click_login(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(LoginPageLocators.login_button)).click()

    def is_logined(self):
        return "" in self.driver.title

    def go_back(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(LoginPageLocators.goback_button)).click()