#NUMEROS PERFEITOS

from re import X

def funçao1(dividendo):
    lista= []
    n= 0
    while dividendo != n:
        n+=1
        if dividendo%n == 0:
            lista.append(n)
        else:
            continue
    del lista[-1]
    return lista

def funçao2(dividendo,divisor):
    soma= 0
    for divisor in divisor:
        soma+= divisor
    if soma == dividendo:
        x= True
    else:
        x= False
    return x

def main():
    for n in range (1, 10001):
        d= funçao1(n)
        p= funçao2(n,d)
        if p == True:
            print(n)

if __name__ == '__main__':
    main()