data = input("Informe uma data dd/mm/aa: ")

meses = ["Janeiro", "Fevereiro", "Marco", "Abril", "Maio", 
"Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

mesesNum = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
cont = 0

listaMes = data.split("/")
novaData = ""

while cont < 11:
    if listaMes[1] == mesesNum[cont]:
        novaData = listaMes[0] + " de "  + meses[cont] + " de " + listaMes[2]
        break
    cont += 1
print(novaData)
