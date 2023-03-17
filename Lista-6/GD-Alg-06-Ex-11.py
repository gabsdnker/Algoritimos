#MEGA-SENA

import random
lista= []

while len(lista) != 6:
    num= random.randint(1,60)
    lista.append(num)
    x= set(lista)
    lista= list(x)

lista.sort()
print(lista)