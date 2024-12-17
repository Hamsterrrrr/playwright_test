from pages.BasePage import BasePage

class LoginPage(BasePage):
    """Страница логина."""

    # Селекторы
    USERNAME_INPUT = "input[id='user-name']"
    PASSWORD_INPUT = "input[id='password']"
    LOGIN_BUTTON = "input[id='login-button']"
    ERROR_MESSAGE = "h3[data-test='error']"

    def login(self, username: str, password: str):
        """Вход в систему с логином и паролем."""
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self) -> str:
        """Получить сообщение об ошибке."""
        return self.get_text(self.ERROR_MESSAGE)

    def is_page_loaded(self) -> bool:
        """Проверка, что страница логина загружена."""
        return self.page.is_visible(self.LOGIN_BUTTON)
