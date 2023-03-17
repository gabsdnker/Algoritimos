#CALCULADORA DE ENVIO E-COMMERCE

#PREÇO DE ENVIO DO PRIMEIRO ITEM R$ 10,95 E PARA MAIS ITENS R$ 2,95 CADA 


def custo(x):
    primeiro_item= 10.95
    demais_itens= (x-1)*2.95
    return (primeiro_item+ demais_itens)
    

def main():
    itens=int(input("Quantidade de itens:  "))
    print(f"R${custo(itens):.2f}")

if __name__== '__main__':
    main()

    
