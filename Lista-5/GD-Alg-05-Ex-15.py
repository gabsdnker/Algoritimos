#DÍGITOS HEXDECIMAIS E DECIMAIS 

#ESCREVER DUAS FUNÇOES: hex2int e int2hex QUE DEVEM FAZER  CONVERSÃO ENTRE DÍGITOS HEXADEIMAIS(0,1,2,3,4,5,6,7,8,9, A,B,C,D,E,F)
# E NÚMEROS INTEIROS NA BASE 10
# A FUNÇAO hex2int DEVE CONVERTER UMA STRING CONTENDO UM UNICO DIGITO HEXADECIMAL EM UM INTEIRO NA BASE 10
#A FUNÇÃO int2hex DEVE CONVERTER UM INTEIRO ENTRE 0 A 15 EM UM UNICO DIGITO HEXADECIMAL 
#Cada função pegará o valor a ser convertido como seu único parâmetro e retornará o valor convertido como o único resultado da função.

def hex2int(hex):
    conversão= int(hex,16)
    return conversão
def int2hex(y):
   x16 = '0 1 2 3 4 5 6 7 8 9 a b c d e f'.upper().split()
   result = []
   while y > 0:
        result.append(x16[(y % 16)])
        y = y // 16
        result.reverse()
        return ''.join(result)

def main():
    s= (input("Digite um hexadecimal: "))
    d= int(input("Digite um decimal: "))
    print("DECIMAL ",hex2int(s),"HEXADECIMAL ", int2hex(d))
    

if __name__=='__main__':
    main()