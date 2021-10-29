import math

import selenium.common.exceptions as exceptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from .locators import BasePageLocators
from .locators import BasketPageLocators


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, selector_type, selector):
        try:
            self.browser.find_element(selector_type, selector)
        except exceptions.NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, selector_type, selector, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(ec.presence_of_element_located((selector_type, selector)))
        except exceptions.TimeoutException:
            return True
        return False

    def is_disappeared(self, selector_type, selector, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, exceptions.TimeoutException).until_not(
                ec.presence_of_element_located((selector_type, selector)))
        except exceptions.TimeoutException:
            return False
        return True

    def does_url_contains_substring(self, url):
        current_url = self.browser.current_url
        if url in current_url:
            return True
        else:
            return False

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except exceptions.NoAlertPresentException:
            print("No second alert presented")

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), \
            "Login link is not presented"

    def go_to_the_basket(self):
        self.browser.find_element(*BasePageLocators.BASKET_BUTTON).click()

        assert self.browser.find_element(*BasketPageLocators.PAGE_TITLE), \
            'This is not a basket page!'
