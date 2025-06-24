import allure
from pages.all_products_page import AllProductsPage
from pages.cart_page import CartPage
from pages.product_page import ProductPage
import pytest

@pytest.mark.usefixtures('user_login')
@allure.feature("Shopping Cart")
class TestAddToCart:

    @allure.story("Add item from products overview")
    @allure.title("Test adding to cart from products page")
    def test_add_to_cart_from_products_page(self, browser):
        products_page = AllProductsPage(browser)
        cart = CartPage(browser)

        with allure.step("Open products page"):
            products_page.open_products_page()

        with allure.step("Add product to cart"):
            products_page.add_product_to_cart()

        with allure.step("Navigate to cart"):
            products_page.go_to_cart()

        with allure.step("Verify cart elements and quantity"):
            cart.check_cart_elements()
            cart.check_qty("1")

    @allure.story("Add item from product detail")
    @allure.title("Test adding to cart from individual product page")
    def test_add_to_cart_from_product_page(self, browser):
        product = ProductPage(browser)
        cart = CartPage(browser)

        with allure.step("Open individual product page"):
            product.open_product_page()

        with allure.step("Add product to cart from detail page"):
            product.add_product_to_cart()

        with allure.step("Navigate to cart"):
            product.go_to_cart()

        with allure.step("Verify cart elements and quantity"):
            cart.check_cart_elements()
            cart.check_qty("1")
