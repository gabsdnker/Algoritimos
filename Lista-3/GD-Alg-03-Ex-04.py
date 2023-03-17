#POLÍGNO REGULAR

poligno= int(input("Digite a quantidade de lados do polígno: "))

if poligno > 10:
    print("ERRO: maior que 10")
elif poligno < 3:
    print("ERRO: menor que 3")
elif poligno == 3:
    print("Triângulo")
elif poligno == 4:
    print("Retângulo")
elif poligno == 5:
    print("Pentágono")
elif  poligno == 6:
    print("Hexágono")
elif poligno == 7:
    print("Heptágono")
elif poligno == 8:
    print("Octógono")
elif poligno == 9:
    print("Eneágono")
else:
    print("Decágono")
