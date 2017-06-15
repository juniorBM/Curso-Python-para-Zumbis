#Lendo o arquivo
# arq = open("numero.txt", "r")
# for linha in arq.readlines():
#     print(linha)
# arq.close

#Jeito Pythonico
with open("numero.txt") as f:
    print(f.read())