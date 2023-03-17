#ORDEM DESCRESCENTE

lista= []
num= 1
while num != 0:
    num= int(input("Digite um número inteiro(0 para parar): "))
    if num == 0:
        break
    elif num != 0:
       lista.append(num) 
       lista.sort()
    else: 
        posição= 0
        while posição < len(lista):
            if num <= lista[posição]:
                lista.insert(posição, num)
                break
            posição= posição+1
            
print(f"Ordem crescente: {lista}")