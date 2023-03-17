#CARTELA DE BINGO

from random import randint

def cartela_de_bingo():
    def criar_lista(x, y):
        conjunto = {0}
        while len(conjunto) != 6:
            valor = randint(x, y)
            conjunto.add(valor)
        conjunto.remove(0)
        lista = list(conjunto)
        lista.sort()            
        return(lista)

    listaB = criar_lista(1, 15)
    listaI = criar_lista(16, 30)
    listaN = criar_lista(31, 45)
    listaG = criar_lista(46,60)
    listaO = criar_lista(61,75)

    dicionario = {"B":listaB, "I":listaI, "N":listaN, "G":listaG, "O":listaO}   
    return(dicionario)  

def main():
    bingo = cartela_de_bingo()
    colunas = bingo.values()
    for item in bingo:
        print(item, end="     ")     
    print()
    print("--------------------------")

    i = 0
    for i in range(5):
        for item in colunas:
            print("%02d" %item[i], end="    ")
        i = i + 1
        print()         

if __name__ == '__main__':
    main()