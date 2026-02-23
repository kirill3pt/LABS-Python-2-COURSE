def convertToMoney():
    money = float(input("Введите сумму (через точку): "))
    rubles = int(money)
    cents = round((money - rubles) * 100)
    if cents >= 100:
        rubles, cents = rubles + 1, cents - 100
    print(f"{rubles} руб. {cents:02d} копеек")