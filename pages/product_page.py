from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_present_success_message(self, product_name=None):
        """Проверяет что сообщение об успешности добавления товара в корзину отображается
        """
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_NAME_IN_MESSAGE_SUCCSESS), 'Success alert is not presented'
        if not product_name:
            product_name = self.get_product_name()
        alert_product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE_SUCCSESS).text
        assert product_name == alert_product_name, \
            f'Product name({product_name}) should be equal alert.text({alert_product_name}) but not'

    def should_be_present_cost_basket_message(self, product_price=None):
        assert self.is_element_present(
            *ProductPageLocators.PRICE_IN_MESSAGE_CHANGE_COST), 'Success alert is not presented'
        if not product_price:
            product_price = self.get_product_price()
        alert_product_price = self.browser.find_element(*ProductPageLocators.PRICE_IN_MESSAGE_CHANGE_COST).text
        assert product_price == alert_product_price, \
            f'Price({product_price}) should be equal alert.text({alert_product_price}) but not'

    def get_product_name(self) -> str:
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_LABEL).text

    def get_product_price(self) -> str:
        return self.browser.find_element(*ProductPageLocators.PRODUCT_COST_LABEL).text

    def should_not_be_success_message(self, timeout=4):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE, timeout), \
            "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self, timeout=4):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE, timeout), \
            "Success message is presented, but should not be"
