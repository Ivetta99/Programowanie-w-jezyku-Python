from magazine import utils
class Product:
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"{self.name}, {utils.info()}"