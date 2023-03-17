#CARACTERE ÚNICO

def caracter(c):
    if len(c) > 256:
        return False
    caract= [False] * 128
    for i in range(0, len(c)):
        val= ord(c[i])
        if caract[val]:
            return False
        caract[val]= True
    return True

def main():
    caract_unico= input("Digite uma palavra: ")
    print(caracter(caract_unico))

if __name__=='__main__':
    main()