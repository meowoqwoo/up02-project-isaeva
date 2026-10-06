"""Проверка класса Product."""
from models import Product


# Создаём один товар вручную
p = Product(
    product_id=1,
    name="Кроссовки Nike Air",
    category="Кроссовки",
    price=8500,
    quantity=3,
    ingredients="ва, в, п",
    photo="photo"
)

print(p.info())
print(f"Со скидкой 25%: {p.price_with_discount(25):.2f} руб.")
