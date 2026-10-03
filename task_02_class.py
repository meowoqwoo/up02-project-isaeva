class Product:
    def __init__(self, name: str, price: float, qty: int):
        self.name = name
        self.price = price
        self.qty = qty

    def total(self) -> float:
        return self.price * self.qty

    def info(self) -> str:
        return f"{self.name}: {self.price} × {self.qty} = {self.total()} руб."


product1 = Product("Кроссовки", 8500, 3)
product2 = Product("Ботинки", 15000, 1)
product3 = Product("Туфли", 12000, 5)

print(product1.info())
print(product2.info())
print(product3.info())
