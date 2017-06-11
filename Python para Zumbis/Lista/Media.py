notas = [10, 5, 6, 9, 2]
cont = 0
media = 0
tamLista = len(notas)

while cont < tamLista:
    media += notas[cont]    
    cont += 1 

media = media / cont

print("A media da notas eh: ", media)