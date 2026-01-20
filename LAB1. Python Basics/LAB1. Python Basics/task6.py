import re

def onceSymbol():
    inputText = input("Введите текст: ")
    counts = {}
    
    for char in inputText:
        counts[char] = counts.get(char, 0) + 1

    for char, count in counts.items():
        if count == 1:
            print(char)