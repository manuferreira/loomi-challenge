from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import NavigationLocators, General, Highlights
from Config import Config
from base_page import BasePage

class MatchesPage(BasePage):
    # missing implementation
    def __init__(self, webdriver, url):
        self.webdriver = webdriver
        self.url = url
        
