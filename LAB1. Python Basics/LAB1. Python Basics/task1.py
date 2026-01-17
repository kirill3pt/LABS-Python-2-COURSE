def convertToMoney():
    money = float(input("Введите сумму(через точку): "))
    rubles = int(money)
    cents = int(round((money - rubles) * 100))
    if (cents >= 100):
        rubles += 1
        cents -= 100
    print(f"{rubles} руб. {cents:02d} копеек ")