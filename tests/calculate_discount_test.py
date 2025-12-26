def calculate_discount(price: float, discount: float) -> float:
    if not 0 <= discount <= 1:
        raise ValueError("discount must be in (0, 1)")

    return price * (1 - discount)


if __name__ == "__main__":
    print(calculate_discount(100, 0.2))
    print(calculate_discount(50, 0))
    print(calculate_discount(200, 1))

    for d in (-0.1, 1.5):
        try:
            print(calculate_discount(100, d))
        except ValueError as e:
            print(f"ValueError for {d}:", e)