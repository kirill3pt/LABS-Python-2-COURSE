def algo():
    password = input("Введите пароль: ")
    countSecurity = 0 #счётчик выполнения критериев безопасности
    print("ВАЖНО! Есть 3 критерия оценки надежности пароля: ")
    print("1 - наличие заглавной буквы;")
    print("2 - наличие цифры, хотя бы одной")
    print("3 - наличие знаков: !?,.:;'")

    count = sum([
        any(char.isdigit() for char in password),
        any(char.isupper() for char in password),
        any(char in "!?,.:;'" for char in password)
    ])

    print(f"Степень защищенности пароля: {count}/3")