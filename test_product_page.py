import time

import pytest

from pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators

nums = [*range(1, 7), pytest.param(7, marks=pytest.mark.xfail), *range(8, 10)]


@pytest.mark.parametrize('num', nums)
def test_guest_can_add_product_to_basket(browser, num):
    base_link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}'
    product_page = ProductPage(browser, base_link)
    product_page.open()
    product_page.add_item_to_basket()
    product_name = product_page.get_product_name()
    product_price = product_page.get_product_price()
    product_page.should_add_correct_product(product_name)
    product_page.should_increase_basket_total_price_correctly(product_price)


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_item_to_basket()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_item_to_basket()
    product_page.should_disappear_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    login_page = product_page.go_to_login_page()
    login_page.should_be_login_page()
