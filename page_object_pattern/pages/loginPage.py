from selenium.webdriver import ActionChains
from page_object_pattern.locators.locators import LoginPageLocators


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)

    def set_create_account(self, email, pass1, pass2):
        self.driver.find_element(*LoginPageLocators.email_textbox).send_keys(email)
        self.driver.find_element(*LoginPageLocators.email_password1).send_keys(pass1)
        self.driver.find_element(*LoginPageLocators.email_password2).send_keys(pass2)
        self.driver.find_element(*LoginPageLocators.create_account_button).click()
        self.driver.find_element(*LoginPageLocators.rules_accept).click()

    def perform_create_account(self):
        self.driver.find_element(*LoginPageLocators.create_account_button).click()

    @property
    def get_error_message(self):
        error_message = self.driver.find_elements(*LoginPageLocators.error_message)
        return [msg.get_attribute('textContent') for msg in error_message]
