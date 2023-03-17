#MÉDIA ARITMÉTICA

nota= float(input("Digite as notas: "))

i= 0
soma= 0
if nota != 0:
    while nota != 0:
        soma= soma+ nota
        i+=1
        nota= float(input("Digite as notas: "))
    else: 
        media= soma/i
        print(media)
else:
    print("erro")




    
    
 
    



