def count_vowels(text: str) -> int:
    vowels = set("aeiouyAEIOUYóÓ")
    return sum(1 for ch in text if ch in vowels)


if __name__ == "__main__":
    print(count_vowels("Python"))
    print(count_vowels("AEIOUY"))
    print(count_vowels("bcd"))
    print(count_vowels(""))
    print(count_vowels("Próba żółwia"))

