#ANO BISSEXTO

ano= int(input("Insira um ano: "))

if (ano%400)== 0:
    print("É ano bissexto")
elif (ano%100)== 0:
    print("Não é ano bissexto")
elif (ano%4)== 0:
    print("É ano bissexto")
else:
    print("Não é ano bissexto")