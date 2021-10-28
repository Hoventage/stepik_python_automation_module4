from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_item_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()
        self.solve_quiz_and_get_code()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.ITEM_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text

    def should_add_correct_product(self, product_name):
        assert product_name == \
               self.browser.find_element(*ProductPageLocators.ITEM_ADDED_MESSAGE).text, \
            'Wrong item has been added to the basket!'

    def should_increase_basket_total_price_correctly(self, product_price):
        assert product_price == \
               self.browser.find_element(*ProductPageLocators.BASKET_TOTAL_PRICE).text, \
            'Wrong basket total price!'
