from pathlib import Path
import re
from collections import Counter

def first():
    filename = input("Введите путь к файлу: ")
    path = Path(filename)
    text = path.read_text(encoding="utf-8").lower()
    letters = re.findall(r"[a-zа-яё]", text)
    freq = Counter(letters)
    for letter, count in freq.most_common():
        print(letter, count)


