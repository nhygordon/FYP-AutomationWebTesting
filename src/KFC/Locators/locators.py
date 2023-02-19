from selenium.webdriver.common.by import By
class MainpageLocators(object):
    app_frame = (By.ID, "frame1")
    loginpage_button = (By.CSS_SELECTOR, "div.login")
    settingpage_button = (By.CSS_SELECTOR, "div.mine")
    profilepage_button = (By.CSS_SELECTOR, "#app > div.mine > div.cellList > div.cellBox.active > div > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > img")
    take_out_button = (By.CSS_SELECTOR, "#main > div.bodyInfo > div.order > div:nth-child(2) > img")
    


class LoginPageLocators(MainpageLocators):
    phonenumber_inputbox = (By.XPATH, "//*[@id='app']/div[1]/div[4]/div/div[1]/input")
    password_inputbox = (By.XPATH, "//*[@id='app']/div[1]/div[4]/div/div[2]/input")
    login_button = (By.CSS_SELECTOR, "div.loginBtn")
    goback_button = (By.CSS_SELECTOR, "#topbar > div.leftIcon")

class ProfilePageLocators(MainpageLocators):
    logout_button = (By.CSS_SELECTOR, "div.btn")
    logout_confirm_button = (By.XPATH, "//*[@id='app']/div[1]/div[5]/div/div[2]/span[2]")

    username_button = (By.CSS_SELECTOR, "#app > div.person > div.personInfo > div.van-cell-group.van-hairline--top-bottom > div:nth-child(1)")
    username_editbox = (By.CSS_SELECTOR, "input.editBox")
    username_edit_confirm_button = (By.CSS_SELECTOR,"#app > div.person > div.confim.active > div > div.btn")

    gender_edit_button = (By.CSS_SELECTOR,"#app > div.person > div.personInfo > div.van-cell-group.van-hairline--top-bottom > div:nth-child(4)")
    gender_M_button = (By.CSS_SELECTOR,"#app > div.person > div.van-popup.van-popup--round.van-popup--bottom.popup > div:nth-child(1)")
    gender_F_button = (By.CSS_SELECTOR,"#app > div.person > div.van-popup.van-popup--round.van-popup--bottom.popup > div:nth-child(2)")
    gender_ND_button = (By.CSS_SELECTOR,"#app > div.person > div.van-popup.van-popup--round.van-popup--bottom.popup > div:nth-child(3)")
    gender_edit_confirm_button = (By.CSS_SELECTOR,"#app > div.person > div.van-popup.van-popup--round.van-popup--bottom.popup > p")
    gender_current_text = By.CSS_SELECTOR,"#app > div.person > div.personInfo > div.van-cell-group.van-hairline--top-bottom > div:nth-child(4) > div.van-cell__value > span"

    left_button = (By.CSS_SELECTOR,"#topbar > div:nth-child(2)")

class TakeOutPageLocators(MainpageLocators):
    selectShop_button = (By.XPATH, "//*[@id='app']/div[1]/div[3]/div/div[4]/div/div[1]/p/span[2]")
    
    
class OrderPageLocators(MainpageLocators):    
    à_la_carte_button = (By.XPATH,"//*[@id='foodList']/div[1]/div[1]/div[1]/div/div[6]/div")

    # à_la_carte_button = (By.CSS_SELECTOR,"#foodList > div.foodList.box > div.category.active > div.category-inner.active > div > div:nth-child(6) > div")
    chooseOriginal_button = (By.CSS_SELECTOR, "#secondFood_13846 > div:nth-child(2) > div > div > div")
    addOriginal_button = (By.CSS_SELECTOR, "#app > div.detailPage > div.skuBox > div > div:nth-child(3) > div > div > div:nth-child(1) > div > div > span")
    addToCart_button = (By.CSS_SELECTOR, "div.detailPage > div.priceBtn")

class EmailPageLocators(MainpageLocators):
    emailpage_button = (By.XPATH,"//*[@id='app']/div[1]/div[3]/span[2]")
    email_inputbox = (By.XPATH, "//*[@id='app']/div[1]/div[4]/div/div[1]/input")
    emailpassword_inputbox = (By.XPATH, "//*[@id='app']/div[1]/div[4]/div/div[2]/input")
    login_button = (By.CSS_SELECTOR, "div.loginBtn")