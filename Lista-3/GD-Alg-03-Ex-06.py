#CLASSIFIQUE O TRIÂNGULO

lado1= int(input("Digite o comprimento do lado 1: "))
lado2= int(input("Digite o comprimento do lado 2: "))
lado3= int(input("Digite o comprimento do lado 3: "))

if lado1== lado2== lado3:
    print("Equilátero")
elif (lado1== lado2) or (lado2== lado3) or (lado1 == lado3):
    print ("Isóceles")

else:
    print("Escaleno")
