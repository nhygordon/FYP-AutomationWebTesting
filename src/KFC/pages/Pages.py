import sys
sys.path.append("./src/KFC")
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.locators import MainpageLocators, LoginPageLocators , ProfilePageLocators, TakeOutPageLocators, OrderPageLocators, EmailPageLocators
from skimage.metrics import structural_similarity
import imutils
import cv2
from PIL import Image

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
    
    def go_takeoutpage(self):
        WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it(MainpageLocators.app_frame))
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
    
    
    

class LoginPage(BasePage):

    def enter_PhoneNumber(self, phonenumber):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LoginPageLocators.phonenumber_inputbox)).clear()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LoginPageLocators.phonenumber_inputbox)).send_keys(phonenumber)

    def enter_Password(self, password):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LoginPageLocators.password_inputbox)).clear()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LoginPageLocators.password_inputbox)).send_keys(password)
    
    def click_login(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(LoginPageLocators.login_button)).click()

    def is_logined(self):
        return "" in self.driver.title

    def go_back(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(LoginPageLocators.goback_button)).click()

class EmailPage(BasePage):
    

    def gotoemailpage(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(EmailPageLocators.emailpage_button)).click()

    def enter_Email(self, email):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(EmailPageLocators.email_inputbox)).clear()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(EmailPageLocators.email_inputbox)).send_keys(email)
    
    def enter_password(self, password):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(EmailPageLocators.emailpassword_inputbox)).clear()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(EmailPageLocators.emailpassword_inputbox)).send_keys(password)

    def click_login(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(EmailPageLocators.login_button)).click()

class ProfilePage(BasePage):
    
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