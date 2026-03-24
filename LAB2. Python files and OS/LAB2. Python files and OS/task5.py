import re

def fifth():
    text = input("Введите текст: ")
    pattern = r"\b[A-Z][a-zA-Z]*\d{2}(?:\d{2})?\b"
    words = re.findall(pattern, text)
    print("Найденные слова:")
    for w in words:
        print(w)
