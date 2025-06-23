from pages.all_products_page import AllProductsPage
from pages.product_page import ProductPage
import pytest


@pytest.mark.usefixture('user_login')
class TestAddToCart:
    def test_add_to_cart_from_products_page(self, browser):
        products_page = AllProductsPage(browser)
        products_page.open_products_page()
        products_page.add_product_to_cart()

    def test_add_to_cart_from_product_page(self, browser):
        product = ProductPage(browser)
        product.open_product_page()
        product.add_product_to_cart()