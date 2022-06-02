from selenium.webdriver.common.by import By


class BasePageLocators:
    cookies = (By.ID, "rodo-ok")


class HomePageLocators:
    add_basket_button = (By.CLASS_NAME, 'promo-day-add-to-basket')
    account_button = (By.XPATH, '/html/body/header/div/div[2]/div[1]/p/a[1]')
    create_account = (By.CLASS_NAME, 'register-link')
    search_input = (By.ID, 'inputSearch')


class SearchResultsPageLocators:
    go_to_book1 = (By.CLASS_NAME, 'e_1gd2-link')
    go_to_book2 = (By.CLASS_NAME, 'e_16k5-link')


class BookPageLocators:
    get_price = (By.ID, 'cena_e')
    add_to_basket1 = (By.ID, 'addToBasket_e_1gd2_ebook')
    add_to_basket2 = (By.ID, 'addToBasket_e_16k5_ebook')
    add_to_basket_gift = (By.XPATH, '//*[@id="box_ebook"]/p[2]/a[2]')


class LoginPageLocators:
    email_textbox = (By.ID, 'email')
    email_password1 = (By.ID, 'haslo1')
    email_password2 = (By.ID, 'haslo2')
    rules_accept = (By.XPATH, '//*[@id="rejestracja"]/fieldset/div[7]/div[4]/label/span[1]')
    create_account_button = (By.XPATH, '//*[@id="rejestracja"]/fieldset/p[2]/button')
    error_message = (By.XPATH, '//div[(@class ="error-info")]//p//label')


class BasketPageLocators:
    basket_how_much = (By.ID, 'koszykbox_ile')
    basket_all_price = (By.ID, 'cart-edit-summary')
    code_input = (By.ID, 'kuponinp')
    code_approve = (By.ID, 'kuponok')
    code_error_msg = (By.XPATH, '//*[@id="formularz"]/div[2]/div[2]/div/div/span')
    gift_msg = (By.XPATH, '/*[@id="e_16k5_ebook"]/td[2]/p[2]/span[3]')