import numbers


while True:
    print("1 - задание №1")
    print("2 - задание №2")
    print("0 - выход")
    ch = input("Выберите задание: ")
    if ch == "1":
        print("ЗАДАНИЕ №1 - ПЕРЕВОД В ДЕНЕЖНЫЙ ФОРМАТ")
        money = float(input("Введите сумму(через точку): "))
        rubles = int(money)
        cents = int(round((money - rubles) * 100))
        print(f"{rubles} руб. {cents:02d} копеек ")
    elif ch == "2":
        print("ЗАДАНИЕ №2 - ПРОВЕРКА НА ВОЗРАСТАНИЕ6")
        def increas(arr):
            for i in range(1, len(arr)):
                if arr[i] <= arr[i - 1]:
                    return False
            return True
        numbersTRUE = [1, 15, 30, 45, 60]
        numbersFALSE = [1, 10, 5, 15, 7]
        print(increas(numbersTRUE))
        print(increas(numbersFALSE))
    elif ch == "0": 
        exit()
    else: 
        print("Ввод неверный. ")