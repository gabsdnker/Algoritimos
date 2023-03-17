#TABELA DE CONVERSÃO DE TEMPERATURA

c= 1
x= 0
print("{:<8} {:<15}".format("Celsius","Fahrenheit"))

while x<10:
    x+=1
    celsius= 10*x
    fahrenheit= (celsius*9/5) + 32
    print("{:<8} {:<15}".format(celsius,fahrenheit))