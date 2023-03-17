#PALÍNDROMO
#letra= y
#conta palavra= z

x= 0
palavra = input("Digite a palavra:")
z= ""

while x < len(palavra):
    y= palavra[x]
    z= y + z
    x+=1
if palavra == z:
        print("Palíndromo")
else:
        print("Não é Palíndromo")
