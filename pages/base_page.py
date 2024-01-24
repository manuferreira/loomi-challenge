from Config import Config
from locators import NavigationLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, webdriver):
        self.webdriver = webdriver
        self.url = Config.BASE_URL
        self.favorites = NavigationLocators.favorites
        self.matches = NavigationLocators.matches
        self.moments = NavigationLocators.moments
        self.calendar = NavigationLocators.calendar

    def go_to_favorites(self):
        WebDriverWait(self.webdriver, Config.ELEMENT_PAGE_MAX).until(EC.visibility_of_element_located(self.favorites))
        self.webdriver.find_element(*self.favorites).click()

    def go_to_matches(self):
        WebDriverWait(self.webdriver, Config.ELEMENT_PAGE_MAX).until(EC.visibility_of_element_located(self.matches))
        self.webdriver.find_element(*self.matches).click()

    def go_to_moments(self):
        WebDriverWait(self.webdriver, Config.ELEMENT_PAGE_MAX).until(EC.visibility_of_element_located(self.moments))
        self.webdriver.find_element(*self.moments).click()

    def go_to_calendar(self):
        WebDriverWait(self.webdriver, Config.ELEMENT_PAGE_MAX).until(EC.visibility_of_element_located(self.calendar))
        self.webdriver.find_element(*self.calendar).click()

    def go_to_kasa(self):
        self.webdriver.get(self.url)


