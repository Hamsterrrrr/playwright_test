from pages.BasePage import BasePage

class CheckoutPage(BasePage):
    """Страница оформления заказа."""

    # Селекторы
    FIRST_NAME_INPUT = "input[id='first-name']"
    LAST_NAME_INPUT = "input[id='last-name']"
    POSTAL_CODE_INPUT = "input[id='postal-code']"
    CONTINUE_BUTTON = "input[id='continue']"
    FINISH_BUTTON = "button[id='finish']"
    SUCCESS_MESSAGE = "h2.complete-header"

    def fill_checkout_form(self, first_name: str, last_name: str, postal_code: str):
        """Заполнение формы оформления заказа."""
        self.fill(self.FIRST_NAME_INPUT, first_name, "Заполнение поля First Name")
        self.fill(self.LAST_NAME_INPUT, last_name, "Заполнение поля Last Name")
        self.fill(self.POSTAL_CODE_INPUT, postal_code, "Заполнение поля Postal Code")
        self.click(self.CONTINUE_BUTTON, "Клик по кнопке Continue")

    def finish_checkout(self):
        """Завершение оформления заказа."""
        self.click(self.FINISH_BUTTON, "Клик по кнопке Finish")

    def get_success_message(self) -> str:
        """Получить сообщение об успешном оформлении."""
        return self.get_text(self.SUCCESS_MESSAGE, "Получение сообщения об успешном заказе")

    def is_page_loaded(self) -> bool:
        """Проверка загрузки страницы."""
        return self.page.is_visible(self.FIRST_NAME_INPUT)
