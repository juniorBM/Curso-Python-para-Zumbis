letras = []
cont = 0
qtdeConsoante = 0

while cont < 10:
    letras.append(input("Palavra: "))
    if letras[cont] not in 'aeiou':
        qtdeConsoante += 1
    cont += 1

print("Quantidade de Consoantes: ", qtdeConsoante)
        