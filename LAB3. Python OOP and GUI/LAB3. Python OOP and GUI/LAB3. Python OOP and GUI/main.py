import Fraction
import BookLibrary
import PhoneFinder
import StringFormatter
import GUIstringFormatter

def main():
    while True:
        print("----------------------------------")
        print("1 - задание №1")
        print("2 - задание №2")
        print("3 - задание №3")
        print("4 - задание №4")
        print("5 - задание №5")
        print("0 - выход")
        print("----------------------------------")
        choice = input("Введите номер задания: ")
        if choice == "1":
            Fraction.run()
        elif choice == "2":
            BookLibrary.run()
        elif choice == "3":
            PhoneFinder.app()
        elif choice == "4":
            StringFormatter.run()
        elif choice == "5":
            GUIstringFormatter.run()
        elif choice == "0":
            break
        else:
            print("Неверный выбор :(")

if __name__ == "__main__": 
    main()