#VALORES DE ENTRADA

n= 0

while True:
    idade= input("Idade: ")
    if not idade:
        break
    else:
        idade= int(idade)
        if (idade<=2):
            valor= 0
        elif (idade>=3) and (idade<=12):
            valor=14
        elif (idade>=65):
            valor=18
        else:
            valor=23
        n= valor +n
print("O valor total foi R$", "%.2f"%n)
