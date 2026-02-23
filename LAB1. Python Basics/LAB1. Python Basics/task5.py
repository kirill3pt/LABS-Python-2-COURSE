import re

def upperReg():
    source_proposal = input("Введите предложение: ")

    parts = re.findall(r"\w+|[^\w\s]+|\s+", source_proposal)
    #\w+ - слово
    #[^\w\s]+ - последовательсность символов, не являющихся словом и пробельным символом
    #\s+ - последовательность пробельных символов
    result = [
        part.upper() if part[0].isupper() else part
        for part in parts
    ]
    out_proposal = "".join(result)
    print(f"Результирующая строка: {out_proposal}")
