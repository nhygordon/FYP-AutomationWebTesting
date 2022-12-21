class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver

class LoginPage(BasePage):

    def enter_phonenumber(self, phonenumber):
        pass
