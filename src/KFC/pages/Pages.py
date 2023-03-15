import sys , os
sys.path.append("./src/KFC")
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Locators.locators import MainpageLocators, Mainpage2Locators, LoginPageLocators , ProfilePageLocators, TakeOutPageLocators, OrderPageLocators, EmailPageLocators
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
        
    
    def go_loginpage(self):
        WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it( MainpageLocators.app_frame))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(MainpageLocators.loginpage_button)).click()
    
    def go_settingpage(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(MainpageLocators.settingpage_button)).click()
    
    def go_profilepage(self):   
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(MainpageLocators.profilepage_button)).click()
    
    def go_takeoutpage(self):
        WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it( MainpageLocators.app_frame))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(MainpageLocators.take_out_button)).click()

    def do_screenshot(self, file_name):
        self.driver.save_screenshot("./Screenshot/{}.png".format(file_name))
    
    def get_visual_compare_result(self,filename):
        #read the image, creating an object
        im = Image.open(r"./src/KFC/Reports/Screenshot/{}.png".format(filename))
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

    # def click_test(self):
    #     element = self.driver.find_element(By.CSS_SELECTOR, "body > div.page-area > div.cookie-area.py-5.position-fixed.start-0.bottom-0.w-100 > div > div > div > div")
    #     loc = element.location
    #     X, Y = loc.get('x'), loc.get('y')
    #     action = ActionChains(self.driver)
    #     action.move_by_offset(X,Y)
    
    def coverage(self):
        obj1_location = (self.driver.find_element(By.CSS_SELECTOR,"body > div.page-area > div.cookie-area.py-5.position-fixed.start-0.bottom-0.w-100")).location
        obj1_size = (self.driver.find_element(By.CSS_SELECTOR,"body > div.page-area > div.cookie-area.py-5.position-fixed.start-0.bottom-0.w-100")).size
        w, h = obj1_size['width'], obj1_size['height']
        
        obj2_location = (self.driver.find_element(By.CSS_SELECTOR,"body > div.page-area > div.footer-area.py-3 > div > div > div.col-sm-8 > div > a:nth-child(3)")).location        
        
        Overlap_area = ((obj2_location["y"] + h) - obj1_location["y"]) * w
        percentage = Overlap_area/ (w * h) * 100

        return percentage
    
class LoginPage(BasePage):
    user_phonenumber = os.getenv('KFC_PN')
    user_password = os.getenv('KFC_PW')
    print(user_password)

    def enter_PhoneNumber(self, phonenumber = user_phonenumber):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LoginPageLocators.phonenumber_inputbox)).clear()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(LoginPageLocators.phonenumber_inputbox)).send_keys(phonenumber)

    def enter_Password(self, password = user_password):
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

class ProfilePage(LoginPage):

    def modify_username(self, username):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(ProfilePageLocators.username_button)).click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(ProfilePageLocators.username_editbox)).send_keys(username)
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(ProfilePageLocators.username_edit_confirm_button)).click()
    
    def modify_gender(self, gender):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(ProfilePageLocators.gender_edit_button)).click()
        time.sleep(1)
        if gender == 'M':
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(ProfilePageLocators.gender_M_button)).click()
        elif gender == 'F':
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(ProfilePageLocators.gender_F_button)).click()
        elif gender == 'ND':
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(ProfilePageLocators.gender_ND_button)).click()
        else :
            print('please retry with M/F/ND')
        #WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(ProfilePageLocators.gender_edit_confirm_button)).click()

    def get_currnet_gender(self):
        current_gender = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(ProfilePageLocators.gender_current_text)).text
        print(current_gender)
        return current_gender
    
    def click_logout(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(ProfilePageLocators.logout_button)).click()
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(ProfilePageLocators.logout_confirm_button)).click()
    
    def left(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(ProfilePageLocators.left_button)).click()

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