import mp3script
import labalchemy
import dbscript
import labmongo
import downloader
import mulmatrix
import checksympy
import countriescheck

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
        print("8 - задание №8")
        print("0 - выход")
        print("----------------------------------")
        choice = input("Введите номер задания: ")
        if choice == "1":
            mp3script.run()
        elif choice == "2":
            dbscript.run()
        elif choice == "3":
            labalchemy.run()
        elif choice == "4":
            labmongo.run()
        elif choice == "5":
            downloader.run()
        elif choice == "6":
            mulmatrix.run()
        elif choice == "7":
            checksympy.run()
        elif choice == "8":
            countriescheck.run()
        elif choice == "0":
            break
        else:
            print("Неверный выбор :(")

if __name__ == "__main__": 
    main()