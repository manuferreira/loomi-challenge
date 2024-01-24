from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import NavigationLocators, General, Highlights
from Config import Config
from base_page import BasePage
from time import sleep

class HighlightsPage(BasePage):
    def __init__(self, webdriver):
        super().__init__(webdriver)
        self.filter_team = Highlights.filter_button
        self.filter_championship = Highlights.filter_button
        self.input_filter = Highlights.filter_input
        self.checkbox = Highlights.checkbox
        self.checkbox_input = Highlights.checkbox_input
        self.highlights_card = Highlights.best_of_card

    def filter_by_team(self, team_name):
        filter_team_button_xpath = self.filter_team[1].format(index=1)

        WebDriverWait(self.webdriver, Config.ELEMENT_PAGE_MAX).until(EC.visibility_of_element_located((self.filter_team[0], filter_team_button_xpath)))

        filter_team_button = self.webdriver.find_element(self.filter_team[0], filter_team_button_xpath)
        filter_team_button.click()
        sleep(5)

        filter_elements_input_field = self.webdriver.find_elements(*self.input_filter)
        input_filter_team = filter_elements_input_field[0]
        input_filter_team.click()
        input_filter_team.send_keys(team_name)
        sleep(5)

        WebDriverWait(self.webdriver, Config.ELEMENT_PAGE_MAX).until(EC.visibility_of_element_located(self.checkbox_input))
        self.webdriver.find_element(*self.checkbox_input).click()

    def filter_by_championship(self, championship_name):
        #bug while trying to filter by championship, some highlights are not shown
        filter_championship_button_xpath = self.filter_team[1].format(index=2)

        WebDriverWait(self.webdriver, Config.ELEMENT_PAGE_MAX).until(EC.visibility_of_element_located((self.filter_championship[0], filter_championship_button_xpath)))

        filter_championship_button = self.webdriver.find_element(self.filter_championship[0], filter_championship_button_xpath)
        filter_championship_button.click()
        sleep(5)

        filter_elements_input_field = self.webdriver.find_elements(*self.input_filter)
        input_filter_championship = filter_elements_input_field[0]
        input_filter_championship.click()
        input_filter_championship.send_keys(championship_name)
        sleep(5)

    def get_team_highlights(self):
        sleep(5)
        get_teams_text = self.webdriver.find_element(*self.highlights_card)
        teams_text = get_teams_text.get_attribute('textContent')
        print(teams_text)

        text_list = teams_text.strip('"').split(' x ')
        return text_list
    
    def get_championship_highlights(self, championship):
        # not able to automate: bug
        pass



        
