from pages.BasePage import BasePage

class CartPage(BasePage):
    """Страница корзины."""

    # Селекторы
    CART_BADGE = "span.shopping_cart_badge"  # Значок с количеством товаров
    CART_BUTTON = "a.shopping_cart_link"     # Кнопка открытия корзины
    CART_ITEMS = "div.cart_item"             # Все элементы корзины
    ITEM_PRICE = "div.inventory_item_price"  # Цена товара
    CHECKOUT_BUTTON = "button[data-test='checkout']"

    def open_cart(self):
        """Открыть корзину."""
        self.click(self.CART_BUTTON)

    def get_cart_count(self) -> int:
        """Получить количество товаров в корзине."""
        if self.page.is_visible(self.CART_BADGE):
            return int(self.get_text(self.CART_BADGE))
        return 0

    def get_cart_items_count(self) -> int:
        """Получить количество товаров в корзине на странице."""
        return len(self.page.query_selector_all(self.CART_ITEMS))

    def get_total_price(self) -> float:
        """Подсчитать сумму цен товаров в корзине."""
        items = self.page.query_selector_all(self.ITEM_PRICE)
        total = sum(float(item.text_content().strip("$")) for item in items)
        return total

    def click_checkout(self):
        """Перейти к оформлению заказа."""
        self.click(self.CHECKOUT_BUTTON)

    def is_page_loaded(self) -> bool:
        """Проверка, что корзина загружена."""
        return self.page.is_visible(self.CART_BUTTON)
