#BINGO: VERIFICANDO A CARTELA VENCEDORA

from audioop import add
import random
from random import randint

def cartelaSorteada():

        def cartela_bingo():

            def criar_lista(x, y):
                conjunto = {100}
                while len(conjunto) != 6:
                    valor = randint(x, y)
                    conjunto.add(valor)
                conjunto.remove(100)
                lista = list(conjunto)        
                lista.sort() 

                lista1 = []           
                for item in lista:
                    item = random.choices([item, 0])
                    lista1.append(item[0])
                return(lista1)

            listaB = criar_lista(1, 15)
            listaI = criar_lista(16, 30)
            listaN = criar_lista(31, 45)
            listaG = criar_lista(46,60)
            listaO = criar_lista(61,75)    

            dicionario = {"B":listaB, "I":listaI, "N":listaN, "G":listaG, "O":listaO}
            return(dicionario)

        bingo = cartela_bingo()
        valores = bingo.values()

        # colunas
        soma_colunas = 0  
        for chaves in bingo:
            soma_colunas = sum(bingo[chaves])
            if soma_colunas == 0:
                coluna = True
                break
            else:
                coluna = False

        #linhas
        soma_linha = 0
        for i in range(5):
            for l in valores:
                soma_linha = soma_linha + l[i]    
            if soma_linha == 0:
                linha = True
                break
            else:
                linha = False
                soma_linha = 0
        
        #diagonal
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
                    soma_diagona_lop = soma_diagona_lop + item
        if soma_diagona_lop == 0 or soma_diagonal == 0:
            diagonal = True
        else:
            diagonal = False
    
        if linha == True:
            tipo = 1
            return(bingo,tipo,"Vencedor")
        elif coluna == True:
            tipo = 2
            return(bingo,tipo,"Vencedor")
        elif diagonal == True:
            tipo = 4
            return(bingo,tipo,"Vencedor")
        else:
            tipo = 8
            return(bingo,tipo,"Não vencedor")
        
def main():
    somatipo = 0
    contipo = {0}
    while somatipo != 15:    

        bingo, tipo , x = cartelaSorteada()        
        if tipo in contipo: 
            continue
        else:
            somatipo = tipo + somatipo
            contipo.add(tipo)

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
            print(x)    

if __name__ == '__main__':
    main()