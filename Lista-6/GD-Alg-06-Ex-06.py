#LISTA DE DIVISORES

def funçao(dividendo):
    lista= []
    n= 0
    while dividendo != n:
        n+=1
        if dividendo%n == 0:
            lista.append(n)
        else:
            continue
    return lista

def main():
    num= int(input("Digite um número inteiro positivo: "))
    print(funçao(num))

if __name__ == "__main__":
    main()