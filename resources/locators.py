from selenium.webdriver.common.by import By


class NavigationLocators:
    favorites = (By.XPATH, '//a[@title="Favoritos"]')
    matches = (By.XPATH, '//a[@title="Partidas"]')
    moments = (By.XPATH, '//a[@title="Melhores momentos"]')
    calendar = (By.XPATH, '//a[@title="Calendário"]')


class General:
    text_p = (By.XPATH, "//p[text()='{text}']")
    button = (By.CSS_SELECTOR, 'data-cy="{text_button}"')
    login_button_base = (By.CSS_SELECTOR, 'button[data-cy="btn-trigger-profile"]')

class Profile:
    login_button_base = (By.CSS_SELECTOR, 'button[data-cy="btn-trigger-profile"]')
    login_profile_base = (By.CSS_SELECTOR, 'div[data-cy="btn-trigger-profile"]')
    email_input = (By.ID, 'email')
    password_input = (By.ID, 'password')
    submit_button = (By.CSS_SELECTOR, 'button[data-cy="login-submit"]')
    email_profile = (By.XPATH, "//p[text()='E-mail']/following-sibling::p")


class FavoriteTeamSearch:
    add_team = (By.XPATH, "//div[p[text()='{team}']]/following-sibling::button[text()='Add']")
    favorited_team = (By.XPATH, "//div[@title='{team}']")
    favorite_match_card = (By.XPATH, "//div[@class='css-7mca6u']//div[2]//p[@title='{team}']")
    remove_teams_button = (By.XPATH, '//button[@class="chakra-button css-di3rc"]')
    div_favorite_team = (By.XPATH, "//div[@class='css-79elbk']")


class Highlights:
    filter_button = (By.XPATH, '(//*[starts-with(@id, "accordion-button-")])[{index}]')
    filter_input = (By.XPATH, '//input[contains(@placeholder, "Pesquisar")]')
    checkbox = (By.XPATH, '//label[contains(@class, "chakra-checkbox")]')
    checkbox_input = (By.XPATH, '//span[@class="chakra-checkbox__control css-2ym9vx"]')
    best_of_card = (By.XPATH, '//p[@class="chakra-text css-1xfi7k7"]')




