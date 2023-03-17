#LETRAS MAIUSCULAS

def letras_maiusculas(x):
    s = ""
    ultimo = ""
    nova_frase= ""
    pontuação= ["!", "?", "."]
    
    for c in x:
        if ultimo == " " and s in pontuação or ultimo== "":
            caracter= c.upper()
            nova_frase=  nova_frase + caracter
        else: 
            nova_frase=  nova_frase + c
        
        if ultimo in pontuação:
            s= ultimo
        elif ultimo.isalpha():
            s= ""
        ultimo= c
    return nova_frase
   
    
def main():
    frase= input("Digite a frase: ")
    print(letras_maiusculas(frase))

if __name__ == '__main__':
    main()
