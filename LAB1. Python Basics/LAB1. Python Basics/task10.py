def algo():
    password = input("Введите пароль: ")
    countSecurity = 0 #счётчик выполнения критериев безопасности
    print("ВАЖНО! Есть 3 критерия оценки надежности пароля: ")
    print("1 - наличие заглавной буквы;")
    print("2 - наличие цифры, хотя бы одной")
    print("3 - наличие знаков: !?,.:;'")

    checkFirst = any(char.isdigit() for char in password) #сначала идет проверка на наличие цифр в строке
    if (checkFirst == True):
        countSecurity += 1 
    checkSecond = any(char.isupper() for char in password) #проверяем наличие любого заглавного символа в строке
    if (checkSecond == True):
        countSecurity += 1
    for char in password:  #проверка наличия знаков препинания в строке
        if char in "!?,.:;'":
            countSecurity += 1
    print("Степень защищенности пароля: {}".format(countSecurity))