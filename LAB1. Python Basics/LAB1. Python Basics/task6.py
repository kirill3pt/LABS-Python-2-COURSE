def onceSymbol():
    inputText = input("Введите текст: ")
    for char in inputText:
        if inputText.count(char) == 1:
            print(char)