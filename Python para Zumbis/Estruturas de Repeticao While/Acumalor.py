# n = 1
# soma = 0
# while n <= 10:
#     x = int(input("Digite o %d numero: " %n))
#     soma = soma + x
#     n = n + 1
# print("Soma: %d" %soma)

# Media de 10 numeros inteiros
# cont = 1
# soma = 0
# while cont <= 10:
#     numeros = float(input("%d Informe qualquer numero: " %cont))
#     soma = soma + numeros
#     cont = cont + 1
# print(soma)
# soma = soma / (cont - 1)
# print("Media: %.2f" %soma)


#Fatorial

num = int(input("Informe um numero inteiro: "))
fat = num
cont = num
while cont > 1:
    fat = fat * (cont - 1)
    cont = cont - 1
print("Fatoria de ", num ," é: ", fat)