#PRECEDÊNCIA DE OPERADORES

def precedencia(x):
    if x == "+" or x == "-":
        inteiro= 1
    elif x == "/" or x == "*":
        inteiro= 2
    elif x == "^":
        inteiro = 3
    else:
        inteiro = -1
    return inteiro

def main():
    operador= input("Digite um operador: ")
    n = precedencia(operador)
    if n == -1:
        print("ERRO[não é um operador]")
    elif n == 1 or n == 2 or n ==3:
        print("O operador é de precedência", n)
if __name__ == '__main__':
    main()