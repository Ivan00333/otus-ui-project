from playwright.sync_api import Page
from assertions.assertions import Assertions
from pages.base_page import BasePage
from locators.product_locators import ProductLocators


class ProductPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.assertions = Assertions(page)

    def open_product_page(self):
        self.open("inventory-item.html?id=5")

    def add_product_to_cart(self):
        self.click(ProductLocators.ADD_TO_CART)
        self.assertions.check_presence(ProductLocators.REMOVE_BUTTON)
        self.assertions.check_presence(ProductLocators.CART_BADGE)