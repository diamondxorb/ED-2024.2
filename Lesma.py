maior_1 = 0
maior_2 = 0
maior_3 = 0

quantidade = int(input())

for i in range(quantidade):
    lesma = int(input())
    if(lesma<10):
        if(lesma>maior_1):
            maior_1 = lesma
    elif(lesma>=10 and lesma<20):
        if(lesma>maior_2):
            maior_2 = lesma
    else:
        if(lesma>maior_3):
            maior_3 = lesma

print(f"{maior_1} {maior_2} {maior_3}")
