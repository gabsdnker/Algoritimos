#JOGO DE BINGO

from random import randint
import random

def cartela_bingo():

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

def colunavence(bingo):
    
        soma_coluna = 0  
        for chaves in bingo:
            soma_coluna = sum(bingo[chaves])
            if soma_coluna == 0:
                return True
            else:
                continue

def vencedor_linha(bingo):
    valores = bingo.values()
    soma_linha = 0
    for i in range(5):
        for l in valores:
            soma_linha = soma_linha + l[i]    
        if soma_linha == 0:
            return True
        else:
            soma_linha = 0
        
def vencedor_diagonal(bingo):
    valores = bingo.values()
    soma_diagonal = 0
    contador = 0
    for lista in valores:
        contador = contador + 1
        contador2 = 0
        for item in lista:
            contador2 = contador2 + 1
            if contador == contador2:
                soma_diagonal = soma_diagonal + item
                
    soma_diagona_lop = 0
    contador3 = 0
    for lista in valores:
        contador3 = contador3 + 1
        contador4 = 0
        for item in lista:
            contador4 = contador4 + 1
            if contador3 + contador4 == 6:
                soma_diagona_lop += item

    if soma_diagona_lop == 0 or soma_diagonal == 0:
        return True

def simulador_bingo():
    bingo = cartela_bingo()
    chamadas_bingo = ["B1","B2","B3","B4","B5","B6","B7","B8","B9","B10","B11","B12","B13","B14","B15","I16","I17","I18","I19","I20","I21","I22","I23","I24","I25","I26","I27","I28","I29","I30","N31","N32","N33","N34","N35","N36","N37","N38","N39","N40","N41","N42","N43","N44","N45","G46","G47","G48","G49","G50","G51","G52","G53","G54","G55","G56","G57","G58","G59","G60","O61","O62","O63","O64","O65","O66","O67","O68","O69","O70","O71","O72","O73","O74","O75"]
    random.shuffle(chamadas_bingo)
    chamadas = 0

    for sorteado in chamadas_bingo:
        chamadas = chamadas + 1
        chave = sorteado[0]
        valor = int(sorteado[1:3])
        if valor in bingo[chave]:
            i = 0
            while i < len(bingo[chave]):  
                if bingo[chave][i] == valor:
                    bingo[chave][i] = 0
                i += 1
        if colunavence(bingo) == True or vencedor_linha(bingo) == True or vencedor_diagonal(bingo)== True:
            break
    
    return(chamadas)

def main():
    todas_chamadas = []
    soma_chamadas = 0
    for n in range(1000):        
        quantidade_chamadas = simulador_bingo()
        soma_chamadas += quantidade_chamadas
        todas_chamadas.append(quantidade_chamadas)
        n += 1 

    print("Mínimo: %.0f"%min(todas_chamadas))
    print("Média: %.0f"%(soma_chamadas/1000))
    print("Máximo: %.0f"%max(todas_chamadas))

if __name__ == '__main__':
    main()