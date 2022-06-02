from page_object_pattern.locators.locators import BasePageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def set_rodo_ok(self):
        self.driver.find_element(*BasePageLocators.cookies).click()