#TABELA DE DESCONTO
 
print("VALOR"," "  "DESCONTADO", " "  "60% DE DESCONTO")

v1= 4.95
n=1

while n <=5:
    d1= v1*0.60
    d2= v1- d1
    print("R$",v1,"  "  "R$","%.2f"%d1," " ,"R$", "%.2f"%d2)
    v1= v1+5
    n+=1



