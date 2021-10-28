import time

import pytest

from .pages.product_page import ProductPage

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
