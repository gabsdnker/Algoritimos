#A LISTA ESTÁ ORDENADA?

from re import X


def ordem(lista):
    crescente= sorted(lista)
    descrescente= sorted(lista, reverse= True)
    if lista == crescente or lista == descrescente:
        x= True
    else:
        x= False
    return x

def main():
    lista= []
    item= input ("Digite um item: ")
    while item != "":
        lista.append(item)
        item= input("Digite um item: ")
    print(ordem(lista))

if __name__ == '__main__':
    main()