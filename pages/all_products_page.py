from playwright.sync_api import Page
from assertions.assertions import Assertions
from pages.base_page import BasePage
from locators.all_products_locators import AllProductsLocators


class AllProductsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.assertions = Assertions(page)

    def open_products_page(self):
        self.open("inventory.html")

    def get_products_list(self):
        return self.get_elements_text_list(AllProductsLocators.ITEM_NAME)

    def add_product_to_cart(self):
        self.click(AllProductsLocators.ADD_TO_CART)
        self.assertions.check_presence(AllProductsLocators.REMOVE_FROM_CART)
        self.assertions.check_presence(AllProductsLocators.CART_BADGE)

    def check_count_product_cards(self, expected_count: int):
        self.assertions.check_count_elements(AllProductsLocators.PRODUCT_CARD, expected_count)

    def check_app_logo_is_presence(self):
        self.assertions.check_presence(AllProductsLocators.APP_LOGO)

    def check_cart_is_presence(self):
        self.assertions.check_presence(AllProductsLocators.SHOPPING_CART)

    def check_product_in_products_list(self, product):
        products_list = self.get_products_list()
        print(products_list)

        assert product in products_list, f"Item with name {product} is not presence on page"