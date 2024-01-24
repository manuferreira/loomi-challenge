from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import NavigationLocators, General, FavoriteTeamSearch
from base_page import BasePage
from Config import Config
from time import sleep

class FavoritesPage(BasePage):
    def __init__(self, webdriver):
        super().__init__(webdriver)
        self.favorite_team_input = (By.CSS_SELECTOR, '[data-cy="input-search-teams"]')
        self.favorite_team_button = (By.CSS_SELECTOR, '[data-cy="btn-favorite-team"]')
        self.favorite_team_name = General.text_p
        self.add_team_button = FavoriteTeamSearch.add_team
        self.conclude_button = (By.CSS_SELECTOR, '[data-cy="btn-submit-teams"]')

        self.edit_teams = (By.CSS_SELECTOR, '[data-cy="btn-edit-teams"]')
        self.remove_team_button = FavoriteTeamSearch.remove_teams_button
        self.save_teams = (By.CSS_SELECTOR, '[data-cy="btn-save-teams"]')

        self.favorite_channel_input = (By.CLASS_NAME, 'input-search-channels')

        self.favorite_matches = (By.CSS_SELECTOR, '.chakra-switch')
        self.favorite_match_card = FavoriteTeamSearch.favorite_match_card

        self.div_team = FavoriteTeamSearch.div_favorite_team


    def select_favorite_team(self, team_name):
        WebDriverWait(self.webdriver, Config.ELEMENT_PAGE_MAX).until(EC.visibility_of_element_located(self.favorite_team_button))
        self.webdriver.find_element(*self.favorite_team_button).click()
        WebDriverWait(self.webdriver, Config.PAGE_LOAD_MAX).until(EC.visibility_of_element_located(self.favorite_team_input))
        self.webdriver.find_element(*self.favorite_team_input).click()
        self.webdriver.find_element(*self.favorite_team_input).send_keys(team_name)

        team_name_xpath = self.favorite_team_name[1].format(text=team_name)
        WebDriverWait(self.webdriver, 8).until(EC.visibility_of_element_located((self.favorite_team_name[0], team_name_xpath)))

        add_team_button_xpath = self.add_team_button[1].format(team=team_name)
        self.webdriver.find_element(self.add_team_button[0], add_team_button_xpath).click()

        self.webdriver.find_element(*self.conclude_button).click()

    def get_favorite_team(self):
        all_favorite_teams = self.webdriver.find_elements(*self.div_team)
        favorite_teams_values = []
        for favorite_team in all_favorite_teams:
            team_text = favorite_team.text
            print(team_text)
            favorite_teams_values.append(team_text)
        return favorite_teams_values

    def remove_teams(self):
        WebDriverWait(self.webdriver, Config.ELEMENT_PAGE_MAX).until(EC.visibility_of_element_located(self.edit_teams))
        self.webdriver.find_element(*self.edit_teams).click()

        WebDriverWait(self.webdriver, 5).until(EC.visibility_of_all_elements_located(self.remove_team_button))
        remove_teams = self.webdriver.find_elements(*self.remove_team_button)

        for delete_team in remove_teams:
            delete_team.click()

        WebDriverWait(self.webdriver, 5).until(EC.element_to_be_clickable(self.save_teams)).click()


    def assert_favorite_matches(self, teams):
        for element in teams:
            match_card = self.favorite_match_card[1].format(team=element)
            try:
                WebDriverWait(self.webdriver, 5).until(EC.visibility_of_element_located((self.favorite_match_card[0], match_card)))

            except Exception as e:
                raise AssertionError(f"There's no matches for the {element}: {e}")

    def check_uncheck_favorite_matches(self, check):
        # not able to implement yet
        pass
