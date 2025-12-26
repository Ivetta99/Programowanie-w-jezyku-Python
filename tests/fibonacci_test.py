def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non‑negative")

    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

if __name__ == "__main__":
    print(fibonacci(0))
    print(fibonacci(1))
    print(fibonacci(5))
    print(fibonacci(10))

    try:
        print(fibonacci(-1))
    except ValueError as error:
        print("ValueError:", error)