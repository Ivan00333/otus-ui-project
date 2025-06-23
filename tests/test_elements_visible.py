import pytest
from pages.all_products_page import AllProductsPage
from locators.all_products_locators import AllProductsLocators


@pytest.mark.usefixtures('user_login')
class TestElementsVisible:
    def test_elements_visible(self, browser):
        products_page = AllProductsPage(browser)
        products_page.open_products_page()
        products_page.check_count_product_cards(expected_count=6)
        products_page.check_cart_is_presence()
        products_page.check_app_logo_is_presence()

    @pytest.mark.parametrize("product_name", AllProductsLocators.PRODUCTS_LIST)
    def test_products_cards(self, browser, product_name):
        products_page = AllProductsPage(browser)
        products_page.check_product_in_products_list(product_name)