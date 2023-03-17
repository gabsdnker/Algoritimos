#EVITANDO DUPLICATAS

#CRIAR UM PROGRAMA QUE LEIA PALAVRAS DO TECLADO ATÉ QUE O USUARIO ENTRE COM UMA PALAVRA VAZIA(ENTER)

#lista = []
#palavras= input("Digite uma palavra: ")
#while True:
 #   if palavras== "":
  #      break
   # else:
    #    palavras= input("Digite uma palavra: ") 
    #lista.append(palavras)

def remove(lista):
    x= set(lista)
    lsta= list(x)
    return lsta

def main():
    listas = []
    palavras= input("Digite uma palavra: ")
    while True:
        if palavras== "":
         break
        else:
         palavras= input("Digite uma palavra: ") 
        listas.append(palavras)
    print(remove(listas))
if __name__== '__main__':
    main()
