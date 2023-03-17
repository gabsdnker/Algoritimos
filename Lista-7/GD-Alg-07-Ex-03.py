#BUSCA REVERSA 

def buscaReversa(dicionário, chave):
    valor = []
    for dicio in dicionário:
        if dicio == chave:
            valor.append(dicionário[dicio])    
    return(valor)

def main():
    d = {1:"g", 2:"a",3:"b",4:"r", 5:"i", 6:"e", 7:"l", 8:"l", 9:"i"}
    c = int(input("Digite a chave: "))
    resultado= (buscaReversa(d, c))
    print(resultado)
if __name__ == '__main__':
    main()
