#HIPOTENUSA
 
from math import sqrt

def hipotenusa(co, ca):
    return sqrt(co ** 2 + ca ** 2)
    
def main():
    x = float( input("Valor do Cateto Oposto: ") )
    y = float( input("Valor do Cateto Adjacente: ") )
    print("Hipotenusa: ",format(hipotenusa(x, y)) )
main()
    

