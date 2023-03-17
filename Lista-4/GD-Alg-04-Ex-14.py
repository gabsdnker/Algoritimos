#BINÁRIO PARA DECIMAL

soma= 0
binario= input("Insira um binário: ")
indice= len(binario)- 1
for digito in binario:
    digito = int(digito) *2**indice
    indice-= 1
    soma= digito +  soma
print(soma)