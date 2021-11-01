import pytest

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

python_everywhere_link = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        link = python_everywhere_link
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.go_to_login_page()
        login_page = LoginPage(browser, link)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = python_everywhere_link
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = python_everywhere_link
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.go_to_the_basket()
    basket_page = BasketPage(browser, link)
    basket_page.should_be_no_goods()
    basket_page.should_be_empty_basket()
