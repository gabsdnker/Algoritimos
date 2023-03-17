#NÚMEROS PRIMOS 

#UM  NÚMERO INTEIRO POSITIVO É PRIMO QUANDO ELE FOR DIVISÍVEL POR 1 OU POR ELE MESMO
#NÚMEROS PRIMOS: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89 e 97.

valor_inteiro= input("Digite um número inteiro positivo: ")

def valor_primo (p):
    cont = 0
    i = 0
    for c in p:
        if i == c or cont < 2:
             i = i + 1
             
        elif x == 0:
            x = c % i
            cont = cont + 1
        elif cont <= 2:
             print("primo")
        else:
            print("não primo")

print(valor_primo(valor_inteiro))
