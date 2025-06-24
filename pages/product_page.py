import allure
from playwright.sync_api import Page
from assertions.assertions import Assertions
from pages.base_page import BasePage
from locators.product_locators import ProductLocators


class ProductPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.assertions = Assertions(page)

    @allure.step("Open product page")
    def open_product_page(self):
        self.open("inventory-item.html?id=5")

    @allure.step("Go to cart from product page")
    def go_to_cart(self):
        self.click(ProductLocators.CART_LINK)

    @allure.step("Add product to cart and verify remove button")
    def add_product_to_cart(self):
        self.click(ProductLocators.ADD_TO_CART)
        self.assertions.check_presence(ProductLocators.REMOVE_BUTTON)

    @allure.step("Check product page elements are present")
    def check_elements_present(self):
        self.assertions.check_presence(ProductLocators.PRODUCT_NAME)
        self.assertions.check_presence(ProductLocators.IMG)
        self.assertions.check_presence(ProductLocators.PRICE)
