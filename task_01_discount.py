price = float(input("Введите цену: "))
discount_percent = float(input("Введите скидку (%): "))


discount_amount = price * (discount_percent / 100)
final_price = price - discount_amount

print(f"Цена со скидкой: {final_price:.2f} руб.")
