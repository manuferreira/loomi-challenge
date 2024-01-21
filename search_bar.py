from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import Config

class SearchBar:
    def __init__(self, webdriver, url):
        self.webdriver = webdriver
        self.url = url
        self.team = (By.ID, 'filter-team')
        self.championship = (By.ID, 'filter-championship')
        self.date = (By.ID, 'popover-trigger-custom-popover')
        self.channel = (By.ID, 'filter-streaming')
        self.submit = (By.CLASS_NAME,'css-n0tora')

    def do_search(self, team=None, championship=None, date=None, channel=None):
        WebDriverWait(self.webdriver, Config.ELEMENT_PAGE_MAX).until(EC.visibility_of_element_located(self.team))

        if team is not None:
            self.webdriver.find_element(*self.team).send_keys(team)
        if championship is not None:
            self.webdriver.find_element(*self.championship).send_keys(championship)
        if date is not None:
            self.webdriver.find_element(*self.date).click()
        if channel is not None:
            self.webdriver.find_element(*self.channel).send_keys(channel)

        self.webdriver.find_element(*self.submit).click()