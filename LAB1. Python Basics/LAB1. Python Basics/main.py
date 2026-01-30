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

#функция вызова скриптов
def main():
    while True:
        print("1 - перевод в деньги")
        print("2 - проверка на возрастание")
        print("3 - номер карты")
        print("4 - разделение по словам")
        print("5 - приведение слов к верхнему регистру")
        print("6 - вывод символов, встречающихся 1 раз")
        print("7 - проверка строк-адресов")
        print("8 - генерация n от 1 до 10000")
        print("9 - имитация работы банкомата")
        print("0 - выход")
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
        elif choice == "0":
            break
        else:
            print("Неверный выбор :(")

if __name__ == "__main__":
    main()