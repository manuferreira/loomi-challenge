from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Config import Config
from base_page import BasePage
from locators import Profile


class Login(BasePage):
    def __init__(self, webdriver):
        super().__init__(webdriver)
        self.login_button = Profile.login_button_base
        self.profile_button = Profile.login_profile_base
        self.email = Profile.email_input
        self.password = Profile.password_input
        self.submit = Profile.submit_button
        self.toggle = (By.CSS_SELECTOR, '.chakra-switch')
        self.email_profile = Profile.email_profile

    def login_button_click(self):
        WebDriverWait(self.webdriver, Config.ELEMENT_PAGE_MAX).until(EC.visibility_of_element_located(self.login_button))

        self.webdriver.find_element(*self.login_button).click()

    def login(self, email, password):
        self.webdriver.find_element(*self.email).send_keys(email)
        self.webdriver.find_element(*self.password).send_keys(password)
        self.webdriver.find_element(*self.submit).click()
        WebDriverWait(self.webdriver, Config.PAGE_LOAD_MAX).until(EC.invisibility_of_element_located(self.submit))

    def get_profile_email(self):
        self.webdriver.find_element(*self.profile_button).click()
        actual_email = self.webdriver.find_element(*self.email_profile).text
        return actual_email

    def connect_google_calendar(self):
        # not able to implement yet
        pass
