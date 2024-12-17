import pytest
import allure
from pages.LoginPage import LoginPage

URL = "https://www.saucedemo.com/"

@allure.feature("Авторизация")
@allure.story("Тесты входа для разных пользователей")
@pytest.mark.parametrize("username, password, expected_result", [
    ("standard_user", "secret_sauce", "https://www.saucedemo.com/inventory.html"),  # Успешный вход
    ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),  # Заблокированный пользователь
    ("", "", "Epic sadface: Username is required"),  # Пустой логин и пароль
    ("standard_user", "", "Epic sadface: Password is required"),  # Пустой пароль
    ("", "secret_sauce", "Epic sadface: Username is required")  # Пустой логин
])
def test_login(browser_page, username, password, expected_result):
    """
    Тест входа в систему:
    - Проверка стандартного пользователя.
    - Проверка заблокированного пользователя.
    - Проверка пустых полей.
    """
    login_page = LoginPage(browser_page)

    with allure.step("Открытие страницы логина"):
        login_page.open(URL)

    with allure.step(f"Попытка входа с данными: {username}/{password}"):
        login_page.login(username, password)

    with allure.step("Проверка результата"):
        if "http" in expected_result:
            # Проверка успешного входа
            assert browser_page.url == expected_result, f"URL не совпадает: {browser_page.url} != {expected_result}"
        else:
            # Проверка сообщения об ошибке
            error_message = login_page.get_error_message()
            assert expected_result in error_message, f"Сообщение об ошибке не совпадает: {error_message} != {expected_result}"
