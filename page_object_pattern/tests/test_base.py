import unittest
from selenium import webdriver
from page_object_pattern.pages.basePage import BasePage


class BaseTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://ebookpoint.pl/")
        self.driver.implicitly_wait(8)
        self.base_page = BasePage(self.driver)
        self.base_page.set_rodo_ok()

    def tearDown(self):
        self.driver.quit()


if  __name__ == '__main__' :
     unittest.main()