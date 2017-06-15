texto = "texto PARA testar metodos"

#Comeca com o que passar no parametro
print(texto.startswith("te"))

#Termina com o que passar no parametro
print(texto.endswith("os"))

#Deixa as letras da palavra tudo em minuscula
print(texto.lower())

#Deixa as letras da palavra tudo em Maiuscula
print(texto.upper())

s = "um tigre, dois tigres, tres tigres"

#Procura a palavra tigre e retorna a posição
print(s.find('tigre'))

#Procura a palavre tigra a partir de uma posição
print(s.find('tigre', 4))

#Se não possuir a palavra é retornado -1
print(s.find('texto'))

#Ele faz uma copia alterando o que passar no parametro para que realmente
#possa substituir é necessario uma atribuição
s = s.replace('tigres', 'gato')
print(s)

#Separa as palavras a partir do espaço entre elas e retorna uma lista
txt = "Analise e Densenvolvimento de Sistemas"
print(txt.split())
data = "21/07/1997"
print(data.split("/"))
ip = "192.145.1.0"
print(ip.split("."))

#Junta as palavras a partir dos parametros passado
texto = ["Uso", "do", "join"]
print(".".join(texto))