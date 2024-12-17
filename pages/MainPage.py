from pages.BasePage import BasePage

class MainPage(BasePage):
    """Главная страница с меню пользователя."""

    # Селекторы
    MENU_BUTTON = "button[id='react-burger-menu-btn']"  # Кнопка открытия меню
    LOGOUT_LINK = "a[id='logout_sidebar_link']"        # Ссылка на выход

    def open_menu(self):
        """Открыть меню."""
        self.click(self.MENU_BUTTON, "Открытие меню пользователя")

    def logout(self):
        """Выполнить выход из аккаунта."""
        self.click(self.LOGOUT_LINK, "Выход из аккаунта")

    def is_page_loaded(self) -> bool:
        """Проверить, что главная страница загружена."""
        return self.page.is_visible(self.MENU_BUTTON)
