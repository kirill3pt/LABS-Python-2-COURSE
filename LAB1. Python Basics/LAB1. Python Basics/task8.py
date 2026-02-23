import random

def generate():
    n = random.randint(1, 10000) #генерация числа n 
    numbers = [random.randint(1, 100) for _ in range(n)]

    size = 1
    while size < n: #в этом цикле находится ближайшая степень двойки, пока size не достигнет n
        size = size * 2
    numbers.extend([0] * (size-n))

    print("n = {}".format(n))
    print("Ближайшая степень двойки = {}".format(size))
    print("Добавлено нулей = {}".format(size - n))
    print("Итоговая длина массива = {}".format(len(numbers)))