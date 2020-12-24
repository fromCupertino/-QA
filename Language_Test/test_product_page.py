from .pages.product_page import PageObject
import pytest
import time


def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = PageObject(browser, link)
    page.open()
    page.add_to_bucket()
    page.solve_quiz_and_get_code()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'
    page = PageObject(browser, link)
    page.open()
    page.add_to_bucket()