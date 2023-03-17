#ORDEM CRESCENTE 

#UM PROGRAMA QUE LEIA NÚMEROS INTEIROS E OS AMARZENA EM UMA LISTA
#PROGRAMA DEVE CONTINUAR LENDO NÚMEROS INTEIROS ATÉ QUE O USUARIO ENTRE COM O VALOR ZERO
#DEVE EXIBIR A ORDEM CRESCENTE DE TODOS OS NÚMEROS DIGITADOS PELO USUÁRIO SEM INCLUIR O VALOR ZERO
#Obs.: você pode implementar o algoritmo de ordenação BubbleSort ou usar o método >>sort<< ou a função >>sorted<< para ordenar a lista.

lista= []
num= 1
while num != 0:
    num= int(input("Digite um número inteiro(0 para parar): "))
    if num == 0:
        break
    elif num != 0:
       lista.append(num) 
    else: 
        posição= 0
        while posição < len(lista):
            if num <= lista[posição]:
                lista.insert(posição, num)
                break
            posição= posição+1
print(f"Ordem crescente: {sorted(lista)}")