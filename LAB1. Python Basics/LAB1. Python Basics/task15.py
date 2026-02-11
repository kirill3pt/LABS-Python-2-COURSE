def pre_process(a=0.97):
    def decorator(func): #func - функция для декорирования
        def wrapper(s, *args, **kwargs): #*args и **kwargs позволяют принимать любое кол-во позиционных и именованных аргументов
            if not s:  #если список пустой
                return func(s, *args, **kwargs)
            #создаём новый список, чтобы не менять оригинал
            filtered = [s[0]]  #первый элемент без изменений
            for i in range(1, len(s)):
                filtered.append(s[i] - a * filtered[i-1])
            return func(filtered, *args, **kwargs)
        return wrapper
    return decorator

@pre_process()
def plot_signal(s):
    for sample in s:
        print(sample)

