palavra = input("Informe um palavra: ")
tamanho = len(palavra)
cont = 0
nova = ""

while cont < tamanho:
    if palavra[cont] in 'aeiou':
        nova = nova + "*"
    else:
        nova = nova + palavra[cont]
    cont += 1
print("Palavra final: ", nova)