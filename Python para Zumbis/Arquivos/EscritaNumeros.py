#Escrita no arquivo
arq = open("numero.txt", "w")
for l in range(1, 101):
    arq.write("%d\n" %l)
arq.close()
