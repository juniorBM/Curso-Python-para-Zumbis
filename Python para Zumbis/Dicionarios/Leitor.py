import string

arq = open('a.txt')
texto = arq.read()
texto = texto.lower()

# for c in string.punctuation:
#     texto = texto.replace(c, ' ')
# texto = texto.split()

# dic = {}

# for p in texto:
#     if p not in dic:
#         dic[p] = 1
#     else:
#         dic[p] += 1

# print("Alice aparece %s vezez" %dic["alice"])
# arq.close()

