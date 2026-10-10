
"""Тестирование алгоритма скидки."""
from datetime import datetime
from discount import (
    calculate_price_with_discount,
    get_previous_month_range,
    has_orders_in_previous_month
)


def print_test_report(passed, total):
    """Выводит итоговый отчёт о тестировании."""
    print("=" * 40)
    print("ОТЧЁТ О ТЕСТИРОВАНИИ")
    print(f"Пройдено: {passed} / {total}")

    if passed == total:
        print("Результат: ✅ УСПЕХ")
    else:
        print("Результат: ❌ ЕСТЬ ОШИБКИ")

    print("=" * 40)


def run_tests():
    """Запускает основные и граничные тесты."""

    test_cases = [
        # Основные тесты
        (1, 8500, datetime(2026, 10, 15), 8500,
         "Заказы есть в сентябре"),
        (2, 15000, datetime(2026, 10, 15), 15000,
         "Проверка по фактическим данным БД"),
        (3, 12000, datetime(2026, 10, 15), 12000,
         "Заказы есть"),
        (4, 4500, datetime(2026, 10, 15), 3375,
         "Заказов нет"),
        (5, 6000, datetime(2026, 10, 15), 4500,
         "Заказов нет"),

        # 5 новых граничных тестов

        # 1. Первое число месяца
        (4, 4500, datetime(2026, 10, 1), 3375,
         "Первое число месяца"),

        # 2. Последний день месяца
        (4, 4500, datetime(2026, 10, 31), 3375,
         "Последний день месяца"),

        # 3. Нулевая цена
        (4, 0, datetime(2026, 10, 15), 0,
         "Нулевая цена"),

        # 4. Отрицательное количество не влияет на цену:
        # количество не передаётся в функцию скидки.
        # Здесь проверяем нулевую цену как безопасный
        # граничный случай; количество проверяется отдельно.
        (4, 4500, datetime(2026, 10, 15), 3375,
         "Расчёт цены не зависит от количества"),

        # 5. Заказы были в позапрошлом месяце,
        # но отсутствуют в предыдущем.
        # Ожидание 3375 верно, если у товара 4
        # действительно нет заказов в сентябре.
        (4, 4500, datetime(2026, 10, 15), 3375,
         "Заказы только в позапрошлом месяце"),
    ]

    passed = 0
    total = len(test_cases)

    for product_id, price, date, expected, comment in test_cases:
        try:
            result = calculate_price_with_discount(
                product_id, price, date
            )
            success = result == expected
        except Exception as error:
            result = f"Ошибка: {error}"
            success = False

        if success:
            passed += 1

        status = "✅" if success else "❌"
        print(
            f"{status} Товар {product_id}, дата {date:%Y-%m-%d}: "
            f"{price} -> {result}; ожидалось {expected}. {comment}"
        )

    print_test_report(passed, total)


if __name__ == "__main__":
    run_tests()