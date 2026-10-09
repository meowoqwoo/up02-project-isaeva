"""Тестирование алгоритма скидки."""
from datetime import datetime
from discount import (
    calculate_price_with_discount,
    get_previous_month_range
)


def run_tests():
    """Запуск тестов расчёта скидки."""

    test_cases = [
        (1, 8500, 8500, datetime(2026, 10, 15),
         "Кроссовки — есть заказы в сентябре"),
        (2, 15000, 11250, datetime(2026, 10, 15),
         "Ботинки — нет заказов в сентябре"),
        (3, 12000, 12000, datetime(2026, 10, 15),
         "Туфли — есть заказы"),
        (4, 4500, 3375, datetime(2026, 10, 15),
         "Сандалии — нет заказов"),
        (5, 6000, 4500, datetime(2026, 10, 15),
         "Кеды — нет заказов"),

        (6, 10000, 7500, datetime(2026, 11, 10),
         "Товар 6 — нет заказов в октябре"),
        (7, 2000, 2000, datetime(2026, 11, 10),
         "Товар 7 — есть заказы в октябре"),
        (8, 4000, 3000, datetime(2026, 3, 15),
         "Товар 8 — нет заказов в феврале"),
        (9, 5000, 5000, datetime(2026, 2, 10),
         "Товар 9 — есть заказы в январе"),
        (10, 12000, 9000, datetime(2026, 1, 15),
         "Товар 10 — нет заказов в декабре прошлого года"),
    ]

    print("=" * 70)
    print("ТЕСТИРОВАНИЕ АЛГОРИТМА СКИДКИ")
    print("=" * 70)

    passed = 0

    for product_id, price, expected, date, comment in test_cases:
        result = calculate_price_with_discount(
            product_id, price, date
        )
        success = result == expected

        if success:
            passed += 1

        status = "OK" if success else "ОШИБКА"
        print(
            f"{status}: товар {product_id}, "
            f"дата {date:%Y-%m-%d}, "
            f"цена {price} -> {result}, "
            f"ожидалось {expected}. {comment}"
        )

    print("-" * 70)
    print(f"Пройдено: {passed} из {len(test_cases)}")

    range_tests = [
        (datetime(2026, 10, 15), ("2026-09-01", "2026-09-30")),
        (datetime(2026, 3, 15), ("2026-02-01", "2026-02-28")),
        (datetime(2026, 1, 15), ("2025-12-01", "2025-12-31")),
    ]

    print("\nПроверка границ предыдущего месяца:")

    for date, expected_range in range_tests:
        result = get_previous_month_range(date)
        success = result == expected_range

        if success:
            passed += 1

        print(
            f"{'OK' if success else 'ОШИБКА'}: "
            f"{date:%Y-%m-%d} -> {result}"
        )

    total = len(test_cases) + len(range_tests)
    print(f"\nИТОГ: пройдено {passed} из {total} проверок")


if __name__ == "__main__":
    run_tests()