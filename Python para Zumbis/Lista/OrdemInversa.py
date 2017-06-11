num = []
cont = 0

while cont < 4:
    num.append(int(input("Informe um numero inteiro: ")))
    cont += 1


cont -= 1

while cont >= 0:
    print("Numero: ", num[cont])
    cont -= 1
