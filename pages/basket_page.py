from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        basket_state = self.browser.find_element(*BasketPageLocators.BASKET_STATE).text

        assert basket_state == 'Your basket is empty. Continue shopping', \
            "Your basket is not empty!"

    def should_not_be_empty_basket(self):
        basket_state = self.browser.find_element(*BasketPageLocators.BASKET_STATE).text

        assert basket_state != 'Your basket is empty. Continue shopping', \
            "Your basket is empty!"

    def should_be_no_goods(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_GOODS_TOTALS), \
            'There are some goods here, basket is not empty!'

    def should_some_no_goods(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_GOODS_TOTALS), \
            'There are some goods here, basket is not empty!'
