def cash():
    request = int(input("Введите необходимую сумму для выдачи денег: "))

    #cashIn - структура (словарь) для хранения купюр разного достоинства, по условию
    cashIn = {
        #5000: 50,
        1000: 100,
        500: 50,
        100: 25,
        50: 20,
        10: 30
        }
    #cashOut - структура (словарь) для запоминания выданных купюр
    cashOut = {} 


    for money in sorted(cashIn.keys(), reverse=True):
        max_needed = request // money #сколько купюр необходимо выдать
        availible = cashIn[money] #сколько всего есть купюр необходимого номинала
        count = min(max_needed, availible) #минимальное из двух переменных выше - сколько в итоге выдавать
        request -= count * money #уменьшается остаток на сумму ту, что выдали
        cashOut[money] = count 

    #вывод
    outputParts = [] #части вывода (например, 5000*1) которые потом будут соединяться в одну строку для вывода
    if request == 0:
        for nominal, count in cashOut.items():
            if count > 0:
                outputParts.append("{}*{}".format(count, nominal)) #соединяем ключ и значение
                outputString = ' + '.join(outputParts) #объединяем результат предыдущих действий
        print(outputString)
    if request > 0:
        print("Операция не может быть выполнена!")