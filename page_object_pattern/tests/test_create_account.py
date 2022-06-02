from page_object_pattern.tests.test_base import BaseTest
from page_object_pattern.pages.homePage import HomePage
from page_object_pattern.pages.loginPage import LoginPage


class TestCreateAccount(BaseTest):

    def test_login_wrong_password(self):
        home_page = HomePage(self.driver)
        home_page.set_create_account_button()
        login_page = LoginPage(self.driver)
        login_page.set_create_account('annakowalska@op.pl', 'haslo1', 'haslo2')
        login_page.perform_create_account()
        error = LoginPage(self.driver)
        error_message = error.get_error_message

        assert error_message[0] == 'Hasła muszą się zgadzać'