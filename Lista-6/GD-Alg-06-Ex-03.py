#REMOVENDO EXTREMOS 

def funcao(lista, n):
        if len(lista) < 4:
            return "PRECISA DE PELO MENOS 4 VALORES"
        else:   
            lista.sort() 
            del lista[:n]
            del lista[-n:] 
            return lista

def main():
    num = input("Digite um número: ")    
    lista = []
    while True:
        if num == "":
            break
        else:
            lista.append(num)
            num = input("Digite um número: ")
    numero = int(input("Digite o número de elementos à remover: ")) 

    print(funcao(lista, numero))

if __name__ == '__main__':
    main()
