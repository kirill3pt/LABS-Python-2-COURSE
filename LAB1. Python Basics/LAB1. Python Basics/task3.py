def numbers():
    numberСard = input("Введите номер карты (16 символов): ")
    if len(numberСard) != 16:
        print("Номер не 16-значный!")
        return
    result = (numberСard[:4] + "*" * 8 + numberСard[12:])