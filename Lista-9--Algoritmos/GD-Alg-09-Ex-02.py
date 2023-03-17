#Exibir o cabeçalho de um arquivo texto.

#Escreva um programa Python que apresente o mesmo comportamento. O programa deve exibir uma mensagem de erro caso não exista o arquivo ou caso não tenha sido passado nenhum argumento para o programa em linha de comando.

#10 primeiras palavras
#arquivo: Palavras_portugues_br-utf8.txt
# AC
# Aarão
# Abel
# Abelardo
# Abissínia
# Abner
# Abraão
# Absalão
# Acab
# Acaia
import sys 

if __name__=='__main__':
    try:
        arquivo= open(sys.argv[1] , "r")
        y=0
        while True:
            x= arquivo.readline()
            y+=1 
            if y == 11:    
                break
            print(x)
        arquivo.close()
    except FileNotFoundError:
        print("ERRO ESSE ARQUIVO NÃO EXITE")
