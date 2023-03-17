#NÍVEIS DE BARULHO

dB= int(input("Insira um valor em decibéis (dB): "))

n1= "Nível 1- Sala silenciosa " #40
n2= "Nível 2- Despertador" #70
n3= "Nível 3- Cortador de grama" #106
n4= "Nível 4- Britadeira" #130

if dB < 40:
    print("O nível de barulho é abaixo do", n1)
elif dB == 40:
    print("O nível de barulho é", n1)
elif dB > 40 and dB < 70:
    print("O nível de barulho está entre", n1, "e", n2)
elif dB == 70:
    print("O nível do barulho é", n2)
elif dB > 70 and dB < 106:
    print("O nível de barulho está entre", n2, "e", n3)
elif dB == 106:
    print("O nível do barulho é", n3)
elif dB > 106 and dB < 130:
    print("O nível de barulho está entre", n3,"e", n4)
elif dB == 130:
    print("O nível do barulho é", n4)
else:
    print("O nível de barulho é acima de",n4)
    
