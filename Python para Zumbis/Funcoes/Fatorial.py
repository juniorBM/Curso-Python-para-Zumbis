def fat():
    num = int(input("Informe um numero inteiro: "))
    fat = num
    cont = num
    while cont > 1:
        fat = fat * (cont - 1)
        cont = cont - 1
    print("Fatoria de ", num ," é: ", fat)

fat()


