palavra = input(str("Informe uma palavra: "))

if palavra == palavra[::-1]:
    print("Palindrome")
else:
    print("Não palindrome")

print(palavra[:: -1])
