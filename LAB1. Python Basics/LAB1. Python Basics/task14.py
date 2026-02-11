def non_empty(func): #func - функция для декорирования
    def wrapper(*args, **kwargs): #*args и **kwargs позволяют принимать любое кол-во позиционных и именованных аргументов
        result = func(*args, **kwargs)
        if isinstance(result, list): #проверка на соответствие: результат - список
            return [item for item in result if item is not None and item != ""] #list comprehension
        #item в result, если item не None или item не пустая строка
        return result
    return wrapper


@non_empty
def get_pages():
    return ["chapter1", '', "contents", '', "line1", None, "hello", "IVT-2"]
