#15. "Tokenização" de strings.

operaçao= input("Digite uma operação: ")

nova_oper= ""
lista= []
for caracter in operaçao:
    if caracter == " ":
        caracter= ""
    nova_oper += caracter

print(nova_oper)
l= ["1","2","3","4","5","6","7","8","9","0"]
antcaracter= ""

for caracter in nova_oper:
    if caracter == "+" or caracter == "-":
        if antcaracter == ")" or antcaracter in l:
            continue
        else:
            o = True
    lista.append(caracter)
    antcaracter= caracter
print(lista)