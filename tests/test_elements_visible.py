import allure
import pytest
from pages.all_products_page import AllProductsPage
from locators.all_products_locators import AllProductsLocators

@allure.feature("Products Page")
@pytest.mark.usefixtures('user_login')
class TestElementsVisible:

    @allure.story("Verify essential elements are visible")
    @allure.title("Test visibility of product page elements")
    def test_elements_visible(self, browser):
        products_page = AllProductsPage(browser)
        with allure.step("Open products page"):
            products_page.open_products_page()
        with allure.step("Check number of product cards"):
            products_page.check_count_product_cards(expected_count=6)
        with allure.step("Verify cart icon is present"):
            products_page.check_cart_is_presence()
        with allure.step("Verify app logo is present"):
            products_page.check_app_logo_is_presence()

    @allure.story("Verify product card listings")
    @allure.title("Test that each product card is listed")
    @pytest.mark.parametrize("product_name", AllProductsLocators.PRODUCTS_LIST)
    def test_products_cards(self, browser, product_name):
        # if product_name == "Sauce Labs Red T-Shirt":
        #     pytest.xfail(reason="bug: этот продукт пока некорректно отображается")

        products_page = AllProductsPage(browser)
        with allure.step(f"Verify presence of product '{product_name}' in list"):
            products_page.check_product_in_products_list(product_name)
