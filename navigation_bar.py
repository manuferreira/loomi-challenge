from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from resources.locators import NavigationLocators
from config.config import Config

class Navigation:
    def __init__(self, webdriver):
        self.webdriver = webdriver
        self.matches = NavigationLocators.matches
        self.moments = NavigationLocators.moments
        self.calendar = NavigationLocators.calendar

    def go_to_matches(self):
        self.webdriver.find_element(*self.matches).click()

    def go_to_moments(self):
        self.webdriver.find_element(*self.moments).click()
    
    def go_to_calendar(self):
        self.webdriver.find_element(*self.calendar).click()

    