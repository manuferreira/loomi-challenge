import unittest
from selenium.webdriver import Chrome
from Config import Config
from login_page import Login
from highlights_page import HighlightsPage


class TestHighlights(unittest.TestCase):
    def setUp(self):
        self.webdriver = Chrome()
        self.webdriver.maximize_window()
        self.login_page = Login(self.webdriver)
        self.highlights_page = HighlightsPage(self.webdriver)
        self.team = "Sport Recife"

    def tearDown(self):
        self.webdriver.quit()

    def test_assert_team_highlights(self):
        self.login_page.go_to_kasa()
        self.login_page.login_button_click()
        self.login_page.login(email=Config.EMAIL, password=Config.PASSWORD)
        self.login_page.go_to_moments()

        self.highlights_page.filter_by_team(team_name=self.team)

        teams = self.highlights_page.get_team_highlights()
        if self.team not in teams:
            raise AssertionError(f"{self.team} not found on: {teams}")

if __name__ == '__main__':
    unittest.main()
