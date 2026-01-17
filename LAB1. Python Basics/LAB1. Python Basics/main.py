import task1
import task2
import task3

def main():
    while True:
        print("1 - перевод в деньги")
        print("2 - проверка на возрастание")
        print("3 - номер карты")
        print("0 - выход")
        choice = input("Введите номер задания: ")
        if choice == "1":
            task1.convertToMoney()
        elif choice == "2":
            arr = [1, 15, 30, 45, 60]
            print(task2.increas(arr))
        elif choice == "3":
            task3.numbers()
        elif choice == "0":
            break
        else:
            print("Неверный выбор :(")

if __name__ == "__main__":
    main()