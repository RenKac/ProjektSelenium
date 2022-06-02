from page_object_pattern.pages.homePage import HomePage
from page_object_pattern.tests.test_base import BaseTest
import page_object_pattern.pages.basketPage

class TestPromoDay(BaseTest):

    def test_promo_day_prices(self):
        home_page = HomePage(self.driver)
        home_page.set_add_promo_book()
        basket_page = page_object_pattern.pages.basketPage.BasketPage(self.driver)
        number_of_books = basket_page.get_check_number_of_book()
        all_prices = basket_page.get_check_prices_all()

        assert number_of_books == '(1)'
        assert all_prices == '9,90 zł'