import pytest
import allure
from pages.LoginPage import LoginPage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage

URL = "https://www.saucedemo.com/"


@allure.feature("Оформление заказа")
@allure.story("Пользователь успешно оформляет заказ")
def test_checkout(browser_page, test_user):
    """
    Тест оформления заказа:
    - Вход пользователя.
    - Добавление товара в корзину.
    - Заполнение формы заказа.
    - Завершение заказа и проверка результата.
    """
    with allure.step("Вход на сайт"):
        login_page = LoginPage(browser_page)
        login_page.open(URL)
        login_page.login(test_user, "secret_sauce")

    with allure.step("Добавление товара в корзину"):
        # Убираем лишний аргумент
        browser_page.click("button[data-test='add-to-cart-sauce-labs-backpack']")

        # Инициализация CartPage
        cart_page = CartPage(browser_page)

    with allure.step("Переход в корзину и проверка товара"):
        cart_page.open_cart()
        cart_count = cart_page.get_cart_count()
        assert cart_count == 1, f"Ожидался 1 товар в корзине, но получено {cart_count}"

    with allure.step("Оформление заказа"):
        cart_page.click_checkout()
        checkout_page = CheckoutPage(browser_page)
        checkout_page.fill_checkout_form("John", "Doe", "12345")
        checkout_page.finish_checkout()

    with allure.step("Проверка сообщения об успешном заказе"):
        success_message = checkout_page.get_success_message()
        assert success_message == "Thank you for your order!", "Сообщение об успешном заказе неверное"
