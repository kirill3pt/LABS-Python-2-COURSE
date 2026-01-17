def numbers():
    numberCard = input("Введите номер карты: 16 символов: ")
    if len(numberCard) == 16:
        result = ""
        for i in range(len(numberCard)):
            if i < 4 or i > 11:
                result += numberCard[i]
            else:
                result += "*"
        print(result)
    else:
        print("Номер не 16-и значный!")