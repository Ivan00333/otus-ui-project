from pages.all_products_page import AllProductsPage
from pages.cart_page import CartPage
from pages.product_page import ProductPage
import pytest


@pytest.mark.usefixtures('user_login')
class TestAddToCart:
    def test_add_to_cart_from_products_page(self, browser):
        products_page = AllProductsPage(browser)
        cart = CartPage(browser)
        products_page.open_products_page()
        products_page.add_product_to_cart()
        products_page.go_to_cart()
        cart.check_cart_elements()
        cart.check_qty("1")


    def test_add_to_cart_from_product_page(self, browser):
        product = ProductPage(browser)
        cart = CartPage(browser)
        product.open_product_page()
        product.add_product_to_cart()
        product.go_to_cart()
        cart.check_cart_elements()
        cart.check_qty("1")

