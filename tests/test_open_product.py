import pytest
from pages.all_products_page import AllProductsPage
from pages.product_page import ProductPage


@pytest.mark.usefixtures('user_login')
class TestOpenProduct:
    def test_open_product(self, browser):
        products_page = AllProductsPage(browser)
        product = ProductPage(browser)
        products_page.open_products_page()
        products_page.open_product()
        product.check_elements_present()
