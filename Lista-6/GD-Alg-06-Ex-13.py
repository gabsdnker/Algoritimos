#CONTAGEM DE ELEMENTOS 

from itertools import count

def contagem(lista,min, max):
    c= 0
    for n in lista:
        if n >= (min) and n< max:
            c=c+1
    return c

def main():
    lsta= []
    valor= input("Digite um valor: ")
    while valor != "":
        lsta.append(int(valor))
        valor= input("Digite um valor: ")
    valor_min= int(input("Digite um valor minimo: "))
    valor_max= int(input("Digite um valor máximo: "))
    x= contagem(lsta, valor_min, valor_max)
    print(x)

if __name__=='__main__':
    main()