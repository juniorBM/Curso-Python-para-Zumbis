minutosGasto = int(input("Informe a quantidade de minutos que voce gastou: "))
conta = 0

# if minutosGasto <= 200 and minutosGasto != 0:
#     conta = minutosGasto * 0.20
# else:
#      if minutosGasto > 200 and minutosGasto <= 400:
#         conta = minutosGasto * 0.18
#      else:
#          if minutosGasto > 400 and minutosGasto <= 799:
#              conta = minutosGasto * 0.15
#          else:
#              conta = minutosGasto * 0.80

if minutosGasto <= 200 and minutosGasto != 0:
    conta = minutosGasto * 0.20
elif minutosGasto > 200 and minutosGasto <= 400:
    conta = minutosGasto * 0.18
elif minutosGasto > 400 and minutosGasto <= 799:
    conta = minutosGasto * 0.15
else:
    conta = minutosGasto * 0.80

print("Valor da Conta: %.2f" %conta)