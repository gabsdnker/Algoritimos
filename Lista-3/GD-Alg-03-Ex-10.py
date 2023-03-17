#COR DA CASA DO TABULEIRO 

posiçao= input("Insira a posição da casa do tabuleiro: ")

l= int(posiçao[1])%2

if (posiçao[0]== "b") or (posiçao[0]== "d") or (posiçao[0]== "f") or (posiçao[0]== "h"):
    c= 0
else: 
    c= 1

if (l== 0) and (c== 0):
    print("A casa", posiçao, "é preta")
elif (l== 1) and (c== 1):
    print("A casa", posiçao, "é preta")
else:
    print("A casa", posiçao, "é branca")