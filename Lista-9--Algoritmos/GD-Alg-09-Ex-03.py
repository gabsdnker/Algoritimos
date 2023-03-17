#Exibir a "cauda" de um arquivo texto.

#Escreva um programa Python que apresente o mesmo comportamento. O programa deve exibir uma mensagem de erro caso não exista o arquivo ou caso não tenha sido passado nenhum argumento para o programa em linha de comando.

#terminal: tail
#Ultima 10 palavras 
# úmidos
# única
# únicas
# único
# únicos
# úrico
# úteis
# útero
# úteros
# útil

import sys 

if __name__=='__main__':
    try:
        arquivo= open(sys.argv[1], "r")
        x= arquivo.readlines()
        y= x[-10:]
        for a in y:
            print(a)
        arquivo.close()
    except FileNotFoundError:
        print("ERRO ESSE ARQUIVO NÃO EXISTE")
