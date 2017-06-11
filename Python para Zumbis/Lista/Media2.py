cont = 0
nota = []
media = 0

while cont < 4:
    nota.append(float(input("Informe uma nota %d: " %cont))) 
    media += nota[cont]
    cont += 1

media = media / cont
print("Media das notas: ", media)