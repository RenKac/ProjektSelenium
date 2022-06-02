from page_object_pattern.tests.test_base import BaseTest
from page_object_pattern.pages.homePage import HomePage
from page_object_pattern.pages.searchResultsPage import SearchResultsPage
from page_object_pattern.pages.bookPage import BookPage
from page_object_pattern.pages.basketPage import BasketPage


class TestBasket(BaseTest):

    def test_total_prices(self):
        home_page = HomePage(self.driver)
        search_page = SearchResultsPage(self.driver)
        book_page = BookPage(self.driver)
        basket_page = BasketPage(self.driver)

        home_page.set_search_item('Python mniej powaznie')
        search_page.set_go_to_book1()
        prices1 = book_page.get_check_prices()
        book_page.set_add_to_basket1()
        home_page.set_search_item('Python mniej powaznie')
        search_page.set_go_to_book2()
        prices2 = book_page.get_check_prices()
        book_page.set_add_to_basket2()

        price_all_basket = basket_page.get_check_prices_all_float()
        number_of_books = basket_page.get_check_number_of_book()
        prices_all = prices1 + prices2

        assert price_all_basket == prices_all
        assert number_of_books == '(2)'

    def test_double_item_in_basket(self):
        home_page = HomePage(self.driver)
        search_page = SearchResultsPage(self.driver)
        book_page = BookPage(self.driver)
        basket_page = BasketPage(self.driver)

        home_page.set_search_item('Python mniej powaznie')
        search_page.set_go_to_book1()
        book_page.set_add_to_basket1()
        home_page.set_search_item('Python mniej powaznie')
        search_page.set_go_to_book1()
        book_page.set_add_to_basket1()

        number_of_books = basket_page.get_check_number_of_book()

        assert number_of_books == '(1)'

    def test_buy_gift(self):
        home_page = HomePage(self.driver)
        search_page = SearchResultsPage(self.driver)
        book_page = BookPage(self.driver)
        basket_page = BasketPage(self.driver)

        home_page.set_search_item('Python mniej powaznie')
        search_page.set_go_to_book1()
        book_page.set_add_to_basket1()
        home_page.set_search_item('Python mniej powaznie')
        search_page.set_go_to_book1()
        book_page.set_add_to_basket_gift()

        number_of_books = basket_page.get_check_number_of_book()

        assert number_of_books == '(1)'

    def test_promo_code(self):
        home_page = HomePage(self.driver)
        search_page = SearchResultsPage(self.driver)
        book_page = BookPage(self.driver)
        basket_page = BasketPage(self.driver)

        home_page.set_search_item('Python mniej powaznie')
        search_page.set_go_to_book1()
        book_page.set_add_to_basket1()
        basket_page.set_code_promo('2za1')

        promo_code_error = basket_page.get_error_code_message()

        assert promo_code_error == 'Kupon nieaktywny'