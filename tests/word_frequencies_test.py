import re
from typing import Dict

def word_frequencies(text: str) -> Dict[str, int]:
    words = re.findall(r"\w+", text.lower(), flags=re.UNICODE)

    freq: Dict[str, int] = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq


if __name__ == "__main__":
    print(word_frequencies("To be or not to be"))

    print(word_frequencies("Hello, hello!"))

    print(word_frequencies(""))

    print(word_frequencies("Python Python python"))

    print(word_frequencies("Ala ma kota, a kot ma Ale."))
