from page_object_pattern.locators.locators import SearchResultsPageLocators


class SearchResultsPage:

    def __init__(self, driver):
        self.driver = driver

    def set_go_to_book1(self):
        self.driver.find_element(*SearchResultsPageLocators.go_to_book1).click()

    def set_go_to_book2(self):
        self.driver.find_element(*SearchResultsPageLocators.go_to_book2).click()