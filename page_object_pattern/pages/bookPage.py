from page_object_pattern.locators.locators import BookPageLocators


class BookPage:

    def __init__(self, driver):
        self.driver = driver

    def set_add_to_basket1(self):
        self.driver.find_element(*BookPageLocators.add_to_basket1).click()

    def set_add_to_basket2(self):
        self.driver.find_element(*BookPageLocators.add_to_basket2).click()

    def get_check_prices(self):
        price = self.driver.find_element(*BookPageLocators.get_price).text
        price_float = float((price[0:len(price) - 3]).replace(",", "."))
        return price_float

    def set_add_to_basket_gift(self):
        self.driver.find_element(*BookPageLocators.add_to_basket_gift).click()
