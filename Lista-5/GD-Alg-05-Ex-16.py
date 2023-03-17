#CONVERSÃO ARBITÁRIA DA BASA NÚMERICA 

#USUARIO ENVIA O NÚMERO PARA CONVERTER UM NÚMERO DE UM BASE PARA BASE 10 E VISE-VERSA
#BASES ENTRE 2 (BINÁRIO) E 16 (HEXADECIMAL) PARA O NÚMERO DE ENTRADAS E O NÚMERO DE RESULTADO 
#DIVIDIR EM VÁRIAS FUNÇÕES: UMA QUE CONVERTE DE UM BASE ARBITARIA EM UMA BASE 10, OUTRA QUE CONVERTE DE BASE 10 PARA BASE ARBITARIA
#1º FUNÇÃO: RECEBE COMO PARAMENTROS UMA STRING COM O NÚMERO A SER CONVEERTIDO PARA BASE 10 E O VALOR DA BASE DESTE NUMERO 
#2º FUNÇÃO: RECEBE PARAMENTROS UM NUMERO NA BASE 10 E A BASE DE QUAL VAI SER CONVERTIDO 

def converter(base, num):
    if base == 1:
        conversão= bin(num)[2:]
    elif base ==2:
        conversão= oct(num)[2:]
    elif base == 3:
        conversão= hex(num)[2:]
    else:
        "Não tem essa opção"
    return conversão

def main():
    num= int(input("Digite um número inteiro(base 10): "))
    base=  int(input("Digite [1] para converter em binário, [2] para converter em octal ou [3] para  converter em hexadecimal: "))
    print(converter(base, num))
if __name__=='__main__':
    main()