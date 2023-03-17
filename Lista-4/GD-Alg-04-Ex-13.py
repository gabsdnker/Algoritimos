#FATORAÇÃO NÚMERICA 

n= int(input("Digite um número inteiro(maior ou igual a 2): "))
fator= 2

while fator <= n :
    if (n%fator==0):
        print(fator)
        n= n/fator
            
    else:
        fator+=1