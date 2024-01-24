import unittest
from selenium.webdriver import Chrome
from Config import Config
from login_page import Login

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.webdriver = Chrome()
        self.webdriver.maximize_window()
        self.login_page = Login(self.webdriver)

    def tearDown(self):
        self.webdriver.quit()

    def test_success_login(self):
        self.login_page.go_to_kasa()
        self.login_page.login_button_click()
        self.login_page.login(email=Config.EMAIL, password=Config.PASSWORD)
        email = self.login_page.get_profile_email()
        self.assertEqual(Config.EMAIL, email, "Different results")

if __name__ == '__main__':
    unittest.main()