while True:
    print("1 - задание №1")
    print("2 - задание №2")
    print("0 - выход")
    ch = input("Выберите задание: ")
    if ch == "1":
        money = float(input("Введите сумму(через точку): "))
        rubles = int(money)
        cents = int(round((money - rubles) * 100))
        print(f"{rubles} руб. {cents:02d} копеек ")
    elif ch == "0": 
        exit()
    else: 
        print("This choice is invalid. ")