from magazine import utils
from magazine.Product import Product

class Order:
    def __init__(self, products: list[Product]) -> None:
        self.products = products

    def __str__(self) -> str:
        return f"Order({len(self.products)} products, {utils.info()})"