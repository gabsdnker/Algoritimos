#NÚMEROS ORDINAIS 

#NÚMEROS INTEIROS DE 1 A 12
#RETORNAR EM STRING (PRIMEIRO, SEGUNDO, TERCEIRO,...)

def numeros_ordinais(n):
        if n == 1:
            print (str("primeiro"))
        elif n == 2:
            print (str("segundo"))
        elif n == 3:
            print (str("terceiro"))
        elif n == 4:
            print (str("quarto"))
        elif n == 5:
            print (str("quinto"))
        elif n == 6:
            print (str("sexto"))
        elif n == 7:
            print (str("sétimo"))
        elif n == 8:
            print (str("oitavo"))
        elif n == 9:
            print (str("nono"))
        elif n == 10:
            print (str("décimo"))
        elif n == 11:
         print (str("décimo primeiro"))
        elif n == 12:
            print (str("décimo segundo"))
        else:
            print("erro")

def main():
    num = int(input("Digite um número:"))
    print(numeros_ordinais(num))
main()
