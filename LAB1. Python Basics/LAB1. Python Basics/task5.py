import re

def upperReg():
    sourceProposal = input("Введите предложение: ")
    words = re.findall(r'\w+|[^\w\s]+|\s+', sourceProposal) 
    #\w+ - слово
    #[^\w\s]+ - последовательсность символов, не являющихся словом и пробельным символом
    #\s+ - последовательность пробельных символов
    proposal = []
    for c in words:
        if c[0].isupper():
            c = c.upper()
            proposal.append(c)
        else:
            proposal.append(c)
        outProposal = ''.join(proposal)
    print("Результирующая строка: {}".format(outProposal))
