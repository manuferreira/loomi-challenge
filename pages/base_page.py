from config.config import Config


class BasePage:
    def __init__(self, webdriver, url):
        self.webdriver = webdriver
        self.url = Config.BASE_URL

    def go_to(self):
        self.webdriver.get(*self.url)


