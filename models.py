"""Модели данных для проекта УП.02."""

from datetime import datetime
from discount import calculate_price_with_discount



class Product:
    """Класс Товар."""

    def __init__(self, product_id, name, ingredients, category, price, quantity, photo):
        """
        Инициализация товара.

        :param product_id: идентификатор
        :param category: категория
        :param name: название
        :param indgredients: состав
        :param price: цена
        :param quantity: количество
        :param photo: фото
        """
        self.id = product_id
        self.category = category
        self.name = name
        self.ingredients = ingredients
        self.price = price
        self.quantity = quantity
        self.photo = photo

    def is_available(self):
        """Возвращает True, если товар есть в наличии."""
        return self.quantity > 0

    def price_with_discount(self, discount_percent):
        """Цена со скидкой."""
        return self.price * (1 - discount_percent / 100)

    def total(self):
        return self.price * self.quantity

    def price_with_discount_auto(self, date=None):
        """Цена со скидкой по алгоритму ДЭ."""
        if date is None:
            date = datetime.now()
        return calculate_price_with_discount(self.id, self.price, date)

    def indicator(self):
        return "много" if self.quantity > 5 else "мало"

    def info(self):
        return (
            f"{self.name} ({self.category}): "
            f"{self.price} руб. × {self.quantity} = {self.total()} руб. "
            f"({self.indicator()})"
        )
    
    def discounted_price(self):
        """Цена со скидкой 25% (упрощённо)."""
        return self.price * 0.80   

class Order:
    """Класс Заказ."""
    def __init__(self, order_id, date, client, product, quantity):
        self.id = order_id
        self.date = date
        self.client = client
        self.product = product      # объект Product
        self.quantity = quantity

    def total(self):
        """Стоимость заказа."""
        return self.product.price * self.quantity

    def info(self):
        return f"Заказ №{self.id} от {self.date}: {self.client} — {self.product.name} × {self.quantity}"

