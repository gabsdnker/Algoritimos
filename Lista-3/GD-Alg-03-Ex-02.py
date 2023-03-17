#IDADE CANINA

idade= float(input("Digite a idade canina: "))

if idade< 0:
    print("ERRO")


else:
    if idade<= 2:
     print(idade*10.5, "Anos")

    else:
        print(((idade-2)*4)+21,"Anos")
   