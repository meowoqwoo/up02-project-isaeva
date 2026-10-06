"""Загрузка заказов из БД в объекты класса Order."""

import sqlite3
from config import DB_PATH
from models import Order
from db_products import get_all_products


def get_all_orders():
    """Возвращает список объектов Order из БД."""
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Заказ ORDER BY id")
    rows = cur.fetchall()
    conn.close()

    products = get_all_products()

    orders = []

    for row in rows:
        product = None

        for p in products:
            if p.id == row[3]:
                product = p
                break

        order = Order(
            order_id=row[0],
            date=row[1],
            client=row[2],
            product=product,
            quantity=row[4]
        )

        orders.append(order)

    return orders


def print_orders(orders):
    """Выводит информацию о заказах."""
    print(f"\nВсего заказов: {len(orders)}\n")

    for order in orders:
        print(order.info())
        print(f"Стоимость: {order.total()}")
        print("-" * 60)


if __name__ == "__main__":
    orders = get_all_orders()
    print_orders(orders)
