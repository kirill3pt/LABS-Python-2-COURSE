#импорт файлов с реализацией заданий лабораторной работы. main необходим для соединения воедино всех файлов
import task1
import task2
import task3
import task4
import task5
import task6
import task7
import task8
import task9
import task10
import task11
import task12
import task13

#функция вызова скриптов
def main():
    while True:
        print("----------------------------------")
        print("1 - перевод в деньги")
        print("2 - проверка на возрастание")
        print("3 - номер карты")
        print("4 - разделение по словам")
        print("5 - приведение слов к верхнему регистру")
        print("6 - вывод символов, встречающихся 1 раз")
        print("7 - проверка строк-адресов")
        print("8 - генерация n от 1 до 10000")
        print("9 - имитация работы банкомата")
        print("10 - проверка надежности пароля")
        print("11 - frange генератор")
        print("12 - get_frames генератор")
        print("13 - extra_enumerate генератор")
        print("0 - выход")
        print("----------------------------------")
        choice = input("Введите номер задания: ")
        if choice == "1":
            task1.convertToMoney()
        elif choice == "2":
            arrTRUE = [1, 15, 30, 45, 60]
            arrFALSE = [2, 1, 15, 10, 7]
            print(task2.increas(arrTRUE))
            print(task2.increas(arrFALSE))
        elif choice == "3":
            task3.numbers()
        elif choice == "4":
            task4.splits()
        elif choice == "5":
            task5.upperReg()
        elif choice == "6":
            task6.onceSymbol()
        elif choice == "7":
            task7.practise()
        elif choice == "8":
            task8.generate()
        elif choice == "9":
            task9.cash()
        elif choice == "10":
            task10.algo()
        elif choice == "11":
            frange = task11.frange(1, 5, 0.1)
            for x in frange:
                print(round(x, 1)) #округление сделано для того чтобы не было проблем в выводе: 1,10000001 и т.д...
        elif choice == "12":
            signal = list(range(10))
            frame = task12.get_frames(signal, 4, 0.75)
            for frames in frame:
                print(frames)
        elif choice == "13":
            x = [1, 3, 4, 2]
            extr = task13.extra_enumerate(x)
            for i, elem, cum, frac in extr:
                print("{}, {}, {}".format(elem, cum, round(frac, 2))) #округление идёт по той же причине, что и в №11
        elif choice == "0":
            break
        else:
            print("Неверный выбор :(")

if __name__ == "__main__":
    main()