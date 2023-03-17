#FORMATANDO UMA LISTA

def formataçao(lista):
    texto= ""
    x= 1
    for item in lista:
        if x== 1:
            texto= item
            x+=1
        elif x == len(lista):
            texto= texto + " e " + item
        else:
            x+=1
            texto= texto + "," + item
    return texto 

def main():
    litens= []
    item= input("Digite um item: ")
    while  item != "":
        litens.append(item)
        item= input("Digite um item: ")
    print(formataçao(litens))

if __name__== '__main__':
    main()