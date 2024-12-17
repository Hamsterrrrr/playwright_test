import pytest
import allure
from pages.LoginPage import LoginPage
from pages.CartPage import CartPage

URL = "https://www.saucedemo.com/"

@allure.feature("Корзина")
@allure.story("Тест добавления товаров в корзину:")
def test_add_to_cart(browser_page, test_user):
    """
    Тест добавления товаров в корзину:
    - Проверка количества добавленных товаров.
    - Проверка общей суммы на основе цен с сайта.
    """
    login_page = LoginPage(browser_page)
    cart_page = CartPage(browser_page)
    
    # Шаг 1: Аутентификация
    login_page.open(URL)
    login_page.login(test_user, "secret_sauce")
    
    # Шаг 2: Добавление товаров
    with allure.step("Добавление товаров в корзину"):
        browser_page.click("button[data-test='add-to-cart-sauce-labs-backpack']")
        browser_page.click("button[data-test='add-to-cart-sauce-labs-bike-light']")
        browser_page.click("button[data-test='add-to-cart-sauce-labs-bolt-t-shirt']")
    
    # Шаг 3: Получение цен товаров
    with allure.step("Получение цен товаров с сайта"):
        price_backpack = float(browser_page.locator("div.inventory_item:has-text('Sauce Labs Backpack') .inventory_item_price").text_content().strip("$"))
        price_bike_light = float(browser_page.locator("div.inventory_item:has-text('Sauce Labs Bike Light') .inventory_item_price").text_content().strip("$"))
        price_bolt_tshirt = float(browser_page.locator("div.inventory_item:has-text('Sauce Labs Bolt T-Shirt') .inventory_item_price").text_content().strip("$"))
        expected_price = price_backpack + price_bike_light + price_bolt_tshirt
    
    # Шаг 4: Проверка количества товаров в корзине
    with allure.step("Проверка количества товаров в корзине"):
        cart_count = cart_page.get_cart_count()
        assert cart_count == 3, f"Ожидалось 3 товара в корзине, но отображается {cart_count}"
    
    # Шаг 5: Переход в корзину и проверка суммы
    with allure.step("Переход в корзину и проверка общей суммы"):
        cart_page.open_cart()
        total_price = cart_page.get_total_price()
        assert total_price == expected_price, f"Ожидаемая сумма {expected_price}, но получено {total_price}"
