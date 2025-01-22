quantidade = int(input())

roupas = input()

alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

alfa_num = []
for i in range(26):
    alfa_num.append(0)

for i in range(0, len(roupas), 3):
    letra = roupas[i]
    numero = roupas[i+1]
    j = 0
    for j in alfabeto:
        if letra == alfabeto[j]:
            alfa_num[j]+=1
