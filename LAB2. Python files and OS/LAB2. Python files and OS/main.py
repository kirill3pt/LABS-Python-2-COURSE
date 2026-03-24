import task1
import task2
import task3
import task4
import task5
import reorganize
import trackmix

def main():
    while True:
        print("----------------------------------")
        print("1 - задание №1")
        print("2 - задание №2")
        print("3 - задание №3")
        print("4 - задание №4")
        print("5 - задание №5")
        print("6 - задание №6")
        print("7 - задание №7")
        print("0 - выход")
        print("----------------------------------")
        choice = input("Введите номер задания: ")
        if choice == "1":
            task1.first()
        elif choice == "2":
            task2.second()
        elif choice == "3":
            task3.third()
        elif choice == "4":
            task4.fourth()
        elif choice == "5":
            task5.fifth()
        elif choice == "6":
            reorganize.run()
        elif choice == "7":
            trackmix.run()
        elif choice == "0":
            break
        else:
            print("Неверный выбор :(")

if __name__ == "__main__": 
    main()