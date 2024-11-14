from math import ceil

total = int(input())

contagem = 0
tempo_total = 0
soma = 0
aux = 0

print(f"Transmitindo {total} bytes...")

while True:
    transmitido = int(input())
    if contagem!=5:
        aux+=transmitido
    contagem+=1
    tempo_total+=1
    soma+=transmitido
    if soma==total:
        break
    if contagem==5:
        if aux!=0:
            tempo = ceil((total-soma)/(aux/5))
            print(f"Tempo restante: {tempo:.0f} segundos.")
        else:
            print("Tempo restante: pendente...")
        contagem = 0
        aux = 0

print(f"Tempo total: {tempo_total} segundos.")
