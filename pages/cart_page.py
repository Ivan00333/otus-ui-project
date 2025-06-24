from playwright.sync_api import Page
from assertions.assertions import Assertions
from pages.base_page import BasePage
from locators.cart_locators import CartLocators


class CartPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.assertions = Assertions(page)

    def check_cart_elements(self):
        self.assertions.check_presence(CartLocators.PRODUCT_NAME)
        self.assertions.check_presence(CartLocators.PRICE)
        self.assertions.check_presence(CartLocators.REMOVE_BUTTON)
        self.assertions.check_presence(CartLocators.CHECKOUT_BUTTON)
        self.assertions.check_presence(CartLocators.CONTINUE_SHOPPING_BUTTON)

    def check_qty(self, count_text: str, ):
        qty = str(self.get_text(CartLocators.QTY))

        assert count_text == qty, f"Expected qty {count_text} actual {qty}"