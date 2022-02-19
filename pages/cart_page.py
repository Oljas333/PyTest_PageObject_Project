from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from .base_page import BasePage
from .locators import CartPageLocators


class CartPage(BasePage):

    def should_be_cart_empty(self, timeout=4):
        assert self.is_not_element_present(*CartPageLocators.LIST_PRODUCTS, timeout), \
            "Cart should be empty, but not"

    def should_be_present_message(self, text, timeout=10):
        assert self.is_element_present(*CartPageLocators.EMPTY_MESSAGE)
        WebDriverWait(self.browser, timeout).until(
            expected_conditions.text_to_be_present_in_element(CartPageLocators.EMPTY_MESSAGE, text)
        )
