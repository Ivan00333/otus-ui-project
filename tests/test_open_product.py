import allure
import pytest
from pages.all_products_page import AllProductsPage
from pages.product_page import ProductPage


@allure.feature("Product Opening")
@pytest.mark.usefixtures('user_login')
class TestOpenProduct:

    @allure.story("Open product details from products page")
    @allure.title("Test opening a product")
    def test_open_product(self, browser):
        products_page = AllProductsPage(browser)
        product = ProductPage(browser)

        with allure.step("Open products page"):
            products_page.open_products_page()

        with allure.step("Open the product detail"):
            products_page.open_product()

        with allure.step("Verify product page elements are present"):
            product.check_elements_present()
