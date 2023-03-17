#SOMENTE PALAVRAS

def funçao(frase):
    lista= [".", ",","!","?",":",";","(",")","-","_"]
    f= ""
    for caracter in frase:
        if caracter in lista:
            caracter= ""
        f= f + caracter
    palavra = f.split(" ")
    return palavra

def main():
    frases= input("Digite a frase: ")
    print(funçao(frases))

if __name__ == '__main__':
    main()