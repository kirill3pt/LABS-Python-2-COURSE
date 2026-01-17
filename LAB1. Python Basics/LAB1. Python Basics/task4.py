import re #для re.split

def splits():
    textString = input("Введите строку: ")
    words = re.split(r'[,.;:\s]+', textString) #разбивается строка по всем возможным разделителям

    group7 = [] #список для слов > 7 символов
    group4to7 = [] #список для слов от 4 до 7 символов
    group4 = [] #список для слов < 4 символов
    
    for c in words: #цикл по каждому слову из списка слов
        if c == '': 
            continue
        length = len(c)
        if length > 7:
            group7.append(c) #добавляем в group7
        elif 4 <= length <= 7:
            group4to7.append(c) #добавляем в group4to7
        else:
            group4.append(c) #добавляем в group4
    #вывод слов, если список не пуст
    if group7:
        print("Слова больше 7 символов:", ' '.join(group7)) 
    if group4to7:
        print("Слова длинной от 4 до 7 символов:", ' '.join(group4to7))
    if group4:
        print("Слова меньше 4 символов:", ' '.join(group4))