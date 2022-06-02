from page_object_pattern.locators.locators import BasketPageLocators


class BasketPage:

    def __init__(self, driver):
        self.driver = driver

    def get_check_number_of_book(self):
        number_of_books = self.driver.find_element(*BasketPageLocators.basket_how_much).text
        return number_of_books

    def get_check_prices_all(self):
        all_prices = self.driver.find_element(*BasketPageLocators.basket_all_price).text
        return all_prices

    def get_check_prices_all_float(self):
        price = self.driver.find_element(*BasketPageLocators.basket_all_price).text
        price_float = float((price[0:len(price) - 3]).replace(",", "."))
        return price_float

    def set_code_promo(self, code):
        self.driver.find_element(*BasketPageLocators.code_input).send_keys(code)
        self.driver.find_element(*BasketPageLocators.code_approve).click()

    def get_error_code_message(self):
        error_message = self.driver.find_element(*BasketPageLocators.code_error_msg).text
        return error_message
