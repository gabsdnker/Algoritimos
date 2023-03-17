#RAÍZES DE EQUAÇÃO QUADRÁTICA

a= int(input("Insira o valor de a: "))
b= int(input("Insira o valor de b: "))
c= int(input("Insira o valor de c: "))

delta= b**2 - 4*a*c

raiz1= (-b + delta**(1/2))/2*a
raiz2= (-b - delta**(1/2))/2*a

if (delta == 0 ):
    print("A expressão possui uma raiz")
    print(raiz1)
elif (delta > 0):
    print("A expressão possui duas raízes")
    print(raiz1, raiz2)
else:
    print("A equação não possui raízes reais")
