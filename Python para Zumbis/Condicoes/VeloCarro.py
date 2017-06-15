velocidade = int(input("Informe a velocidade do carro: "))

if velocidade > 110:
    print("Voce foi multado")
    valorMulta = (velocidade - 110) * 5
    print("O valor da multa eh: ", valorMulta)
else:
    print("Voce não sera multado")