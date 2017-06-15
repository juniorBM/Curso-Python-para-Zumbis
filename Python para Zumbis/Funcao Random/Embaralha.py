import random

def embaralha(texto):
    random.shuffle(texto)
    print("".join(texto))


texto = list(input("Informe uma palavra: "))

embaralha(texto)