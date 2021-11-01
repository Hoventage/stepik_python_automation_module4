import time

import pytest

from .pages.base_page import BasePage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage

nums = [*range(1, 7), pytest.param(7, marks=pytest.mark.xfail), *range(8, 10)]
coders_at_work_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
the_city_and_the_stars_link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"


@pytest.mark.parametrize('num', nums)
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, num):
    base_link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}'
    product_page = ProductPage(browser, base_link)
    product_page.open()
    product_page.add_item_to_basket_and_solve_quiz()
    product_name = product_page.get_product_name()
    product_price = product_page.get_product_price()
    product_page.should_add_correct_product(product_name)
    product_page.should_increase_basket_total_price_correctly(product_price)


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = coders_at_work_link
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_item_to_basket()
    product_page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = coders_at_work_link
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = coders_at_work_link
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_item_to_basket()
    product_page.should_disappear_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = the_city_and_the_stars_link
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = the_city_and_the_stars_link
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_login_page()
    login_page = LoginPage(browser, link)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = the_city_and_the_stars_link
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_the_basket()
    basket_page = BasketPage(browser, link)
    basket_page.should_be_no_goods()
    basket_page.should_be_empty_basket()


class TestUserAddToBasketFromProductPage:
    link = coders_at_work_link

    @pytest.fixture(scope='function')
    def setup(self, browser):
        time_for_credentionals = str(time.time())
        email = time_for_credentionals + "@fakemail.org"
        password = 'test_' + time_for_credentionals

        base_page = BasePage(browser, self.link)
        base_page.open()
        base_page.go_to_login_page()
        login_page = LoginPage(browser, self.link)
        login_page.should_be_login_page()
        login_page.register_new_user(email=email, password=password)
        base_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser, setup):
        product_page = ProductPage(browser, self.link)
        product_page.open()
        product_page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, setup):
        product_page = ProductPage(browser, self.link)
        product_page.open()
        product_page.add_item_to_basket()
        product_name = product_page.get_product_name()
        product_price = product_page.get_product_price()
        product_page.should_add_correct_product(product_name)
        product_page.should_increase_basket_total_price_correctly(product_price)
