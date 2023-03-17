#CIFRA DE CESAR

#mensagem= m
#deslocamento= d
#concatenar= c

m= input("Digite a mensagem: ")
d= int(input("Digite a distância do deslocamento: "))
a= 1
c= " "

for letra in m:
    x= (ord(letra))
    x= x + d
    if x > 122:
        x= x - 26
    elif x > 90 and x < 97:
        x= x - 26
    b= (chr(x))
    c= c + b 
print(c)