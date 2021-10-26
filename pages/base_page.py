import selenium.common.exceptions as exceptions


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, selector_type, selector):
        try:
            self.browser.find_element(selector_type, selector)
        except exceptions.NoSuchElementException:
            return False
        return True

    def does_url_contains_substring(self, url):
        current_url = self.browser.current_url
        if url in current_url:
            return True
        else:
            return False


