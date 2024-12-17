import os
import allure
from datetime import datetime
from abc import ABC, abstractmethod
from playwright.sync_api import Page

class BasePage(ABC):
    def __init__(self, page: Page):
        self.page = page

    @abstractmethod
    def is_page_loaded(self) -> bool:
        """Проверка, что страница загружена."""
        pass

    def open(self, url: str):
        """Открыть страницу и сделать скриншот."""
        self.page.goto(url)
        self.attach_screenshot("open_page")

    def click(self, locator: str, name: str = "click_action"):
        """Клик по элементу и скриншот."""
        self.page.click(locator)
        self.attach_screenshot(name)

    def fill(self, locator: str, value: str, name: str = "fill_input"):
        """Заполнить поле и сделать скриншот."""
        self.page.fill(locator, value)
        self.attach_screenshot(name)

    def get_text(self, locator: str, name: str = "get_text"):
        """Получить текст элемента и сделать скриншот."""
        text = self.page.text_content(locator)
        self.attach_screenshot(name)
        return text

    def attach_screenshot(self, name: str):
        """Сохранить скриншот и прикрепить к Allure."""
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"screenshots/{name}_{timestamp}.png"
        os.makedirs("screenshots", exist_ok=True)
        self.page.screenshot(path=filename)
        allure.attach.file(filename, name=name, attachment_type=allure.attachment_type.PNG)
