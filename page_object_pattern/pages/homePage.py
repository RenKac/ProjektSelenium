from page_object_pattern.locators.locators import HomePageLocators
from selenium.webdriver import ActionChains, Keys


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)

    def set_create_account_button(self):
        self.action.move_to_element(self.driver.find_element(*HomePageLocators.account_button)).perform()
        self.driver.find_element(*HomePageLocators.create_account).click()

    def set_search_item(self, title):
        self.driver.find_element(*HomePageLocators.search_input).send_keys(title + Keys.ENTER)

    def set_add_promo_book(self):
        self.driver.find_element(*HomePageLocators.add_basket_button).click()
