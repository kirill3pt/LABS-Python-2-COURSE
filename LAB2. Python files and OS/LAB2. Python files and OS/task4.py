import re

def fourth():
    filename = input("Введите имя файла: ")
    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()
    pattern = r"\(\d{3}\)\d{7}|\(\d{3}\)\d{3}-\d{2}-\d{2}"
    phones = re.findall(pattern, text)
    print("Найденные номера:")
    for p in phones:
        print(p)
   