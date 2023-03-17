#RAIZ QUADRADA

import math


while True:
    x= int(input("Digite o valor de x: "))
    a= x/2
    y = x
    y = (x + a/x) / 2
    if y == x:
        break
    x = y
    print(x)
