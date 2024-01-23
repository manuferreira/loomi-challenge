from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from resources.locators import NavigationLocators, General, Highlights
from config.config import Config
from pages.base_page import BasePage

class MatchesPage(BasePage):
    # missing implementation
    def __init__(self, webdriver, url):
        self.webdriver = webdriver
        self.url = url
        