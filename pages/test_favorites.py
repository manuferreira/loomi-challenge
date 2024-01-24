import unittest
from selenium.webdriver import Chrome
from login_page import Login
from Config import Config
from favorites_page import FavoritesPage

class TestFavorites(unittest.TestCase):
    def setUp(self):
        self.webdriver = Chrome()
        self.webdriver.maximize_window()
        self.login_page = Login(self.webdriver)
        self.favorites_page = FavoritesPage(self.webdriver)
        self.favorite_team_name = ["Sport Recife", "Palmeiras"]
        self.login_page.go_to_kasa()
        self.login_page.login_button_click()
        self.login_page.login(email=Config.EMAIL, password=Config.PASSWORD)

    def tearDown(self):
        self.favorites_page.remove_teams()
        self.webdriver.quit()

    def test_add_favorite_team(self):
        self.login_page.go_to_favorites()
        self.favorites_page.select_favorite_team(team_name=self.favorite_team_name[0])
        self.favorites_page.select_favorite_team(team_name=self.favorite_team_name[1])

    def test_check_favorite_team(self):
         self.login_page.go_to_favorites()
         self.favorites_page.select_favorite_team(team_name=self.favorite_team_name[0])
         self.favorites_page.select_favorite_team(team_name=self.favorite_team_name[1])

         favorite_team = self.favorites_page.get_favorite_team()
         for team in favorite_team:
             self.assertEqual(self.favorite_team_name, team, "Different results")


if __name__ == '__main__':
    unittest.main()
