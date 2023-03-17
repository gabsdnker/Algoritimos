 #SENHA ALEATÓRIA 

#A SENHA DEVE TER UM COMPRIMENTO ALEATÓRIO DE 7 A 10 CARACTERES 
#CADA CARACTER DEVE SER SELECIONADO ALEATORIAMENTE DAS POSIÇÕES 33 A 126 NA TABELA ASCII
# SUA FUNÇÃO NÃO RECEBE NENHUM PARAMETRO 
# RETORNARÁ A SENHA GERADA ALEATORIAMENTE COMO SEU ÚNICO RESULTADO 
# FUNÇÃO chr

import random

def senha_aleatoria():
    comprimento= random.randint(7,11)
    i= 0
    senha= ""
    while i != comprimento:
        caracter= random.randint(33,127)
        c= chr(caracter)
        senha= senha + c
        i+=1
    return senha

def main():
    print(senha_aleatoria())

if __name__=='__main__':
    main()
