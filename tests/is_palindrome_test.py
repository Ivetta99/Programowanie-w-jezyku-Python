def is_palindrome(text: str) -> bool:
    clean = text.replace(" ", "").lower()
    return clean == clean[::-1]


# Proste sprawdzenie testów z polecenia:
if __name__ == "__main__":
    print(is_palindrome("kajak"))
    print(is_palindrome("Kobyła ma mały bok"))
    print(is_palindrome("python"))
    print(is_palindrome(""))
    print(is_palindrome("A"))