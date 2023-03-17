#MEDIANA DE TRÊS VALORES

def mediana(n1,n2,n3):
    if (n1 > n2 and n2 > n3) or (n3 > n2 and n2 > n1):
       m= n2

    elif (n2 > n3 and n3 > n1) or (n1 > n3 and n3 > n2):
        m= n3

    else:
        m= n1
    return m

def main():
    numero1= (input("Valores: "))
    numero2= (input("Valores: "))
    numero3= (input("Valores: "))
    print(mediana(numero1, numero2, numero3))

if __name__ ==  '__main__':
    main()
