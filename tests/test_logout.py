import pytest
import allure
from pages.LoginPage import LoginPage
from pages.MainPage import MainPage

URL = "https://www.saucedemo.com/"


@allure.feature("Выход из аккаунта")
@allure.story("Проверка корректности выхода и недоступности защищённых страниц")
def test_logout(browser_page, test_user):
    """
    Тест выхода из аккаунта:
    - Вход в систему.
    - Открытие меню.
    - Выход из аккаунта.
    - Проверка недоступности защищённой страницы.
    """
    with allure.step("Вход в систему"):
        login_page = LoginPage(browser_page)
        login_page.open(URL)
        login_page.login(test_user, "secret_sauce")

    with allure.step("Открытие меню и выход из аккаунта"):
        main_page = MainPage(browser_page)
        main_page.open_menu()
        main_page.logout()

    with allure.step("Проверка недоступности защищённой страницы"):
        # Попытка зайти на защищённую страницу после выхода
        browser_page.goto("https://www.saucedemo.com/inventory.html")
        assert browser_page.url == URL, "После выхода защищённая страница остаётся доступной"
