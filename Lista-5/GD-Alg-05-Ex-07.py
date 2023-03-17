#TRIÂNGULO VÁLIDO?

#POSSUI 3 CANUDOS COM O MESMO TAMANHO CADA CANUDO FORMA UM TRIÂNGULO 
#SE O COMPRIMENTO DE UM DOS CANUDOS FOREM MAIOR OU IGUAL A SOMA DOS DOIS OUTROS CANUDOS NÃO FORMARÁ UM TRIÂNGULO

def triangulo (a, b,c):
    if a>=b+c or b>=c+a or c>=a+b :
        resultado = print("não válido")
    elif a== b and b== c:
        resultado= print( "Triângulo válido")

    return resultado

def main():
    x = input("Valor do lado 1: " )
    y = input("Valor do lado 2: " )
    z= input("Valor do lado 3: ")
    print(triangulo(x,y,z))

if __name__== '__main__':
    main()
