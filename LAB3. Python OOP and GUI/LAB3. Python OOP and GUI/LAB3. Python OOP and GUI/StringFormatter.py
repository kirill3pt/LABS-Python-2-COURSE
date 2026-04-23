import re

class StringFormatter:
    def __init__(self, text, separators=" "):
        self.text = text
        self.separators = separators

    def __str__(self):
        return self.text

    def _split_words(self):
        return re.split(r"[,\s]+", self.text)

    def remove_short_words(self, n):
        words = self._split_words()
        self.text = " ".join([w for w in words if len(w) >= n])
        return self

    def mask_digits(self):
        self.text = re.sub(r"\d", "*", self.text)
        return self

    def spaced_chars(self):
        self.text = " ".join(self.text)
        return self

    def sort_by_length(self):
        words = self._split_words()
        words.sort(key=len)
        self.text = " ".join(words)
        return self

    def sort_lex(self):
        words = self._split_words()
        words.sort()
        self.text = " ".join(words)
        return self

def run():
    text = input("Введите строку: ")
    sf = StringFormatter(text)

    while True:
        print("\n1 - удалить короткие слова")
        print("2 - заменить цифры на *")
        print("3 - пробелы между символами")
        print("4 - сортировка по длине")
        print("5 - лексикографическая сортировка")
        print("0 - выход")

        choice = input("Выбор: ")

        if choice == "1":
            n = int(input("n = "))
            sf.remove_short_words(n)
            print(sf)

        elif choice == "4":
            sf.sort_by_length()
            print(sf)

        elif choice == "5":
            sf.sort_lex()
            print(sf)

        elif choice == "2":
            sf.mask_digits()
            print(sf)

        elif choice == "3":
            sf.spaced_chars()
            print(sf)

        elif choice == "0":
            break