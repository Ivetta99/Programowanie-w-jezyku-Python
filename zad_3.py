class Property:
    def __init__(self, area, rooms, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"{self.address}, {self.area} m2, rooms: {self.rooms}, price: {self.price} zl"

class House(Property):
    def __init__(self, area, rooms, price, address, plot):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        base = super().__str__()
        return f"House: {base}, plot: {self.plot} m2"

class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        base = super().__str__()
        return f"Flat: {base}, floor: {self.floor}"


house = House(
    area=120,
    rooms=5,
    price=950000,
    address="Kraków, Długa 10",
    plot=500
)

flat = Flat(
    area=45,
    rooms=2,
    price=520000,
    address="Warszawa, Prosta 5/12",
    floor=3
)

print(house)
print(flat)
