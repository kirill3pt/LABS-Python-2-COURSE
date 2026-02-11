def extra_enumerate(x):
    total = sum(x) #сумма всех элементов
    cum = 0 #накопленная сумма на момент текущей итерации

    for i, elem in enumerate(x): 
        cum += elem #обновляем накопленную сумму
        frac = cum / total #находим часть от всей суммы
        yield i, elem, cum, frac #возвращаем значения
