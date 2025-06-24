

class AllProductsLocators:
    PRODUCT_CARD = "//div[@data-test='inventory-item']"
    ITEM_NAME = "//div[@data-test='inventory-item-name']"
    APP_LOGO = "//div[@class='app_logo']"
    SHOPPING_CART = "//a[@data-test='shopping-cart-link']"
    ADD_TO_CART = "//button[@data-test='add-to-cart-sauce-labs-backpack']"
    REMOVE_FROM_CART = "//button[@data-test='remove-sauce-labs-backpack']"
    CART_BADGE = "//span[@data-test='shopping-cart-badge']"
    BACKPACK_LABEL = "//div[text()='Sauce Labs Backpack']"
    CART_LINK = "//a[@data-test='shopping-cart-link']"

    PRODUCTS_LIST = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie",
        "Sauce Labs Bike Light",
        "Sauce Labs Fleece Jacket",
        "Sauce Labs Red T-Shirt"
    ]