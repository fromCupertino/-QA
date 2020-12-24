from .base_page import BasePage
from .locators import ProductPageLocators
import time


class PageObject(BasePage):
    def add_to_bucket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BUCKET)
        add_button.click()

    def book_name(self):
        bookname = self.browser.find_element(*ProductPageLocators.BOOKNAME)
        return bookname.text

    def sucmesg(self):
        meseg = self.browser.find_element(*ProductPageLocators.SUCCES_MESSAGE)
        return meseg.text
