#NEGATIVOS, ZEROS E POSITIVOS

lista= []
num= input("Digite um número: ")

while num != " ":
    lista.append((num))
    if num == "":
        break
    num= input("Digite um número: ")

lista.sort()
for numeros in lista:
 print(numeros)