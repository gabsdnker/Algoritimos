#APROXIMAÇÃO DO VALOR DE PI

a= 1
n1= 0
n2= 1
n3= 2
n= 0
old= 0

while a <= 15:
    a= a + 1
    n1= n1 + 2
    n2= n2 + 2
    n3= n3 + 2
    n= 4/((n1)*(n2)*(n3))
    if a%2 == 0:
        old= old + n
        soma= 3 + old + n
    else:
        old= old - n
        soma= 3 + old - n
print("\t", end=" ")
for coluna in range (1,16):
    print (coluna,soma, "\t", end=" ")