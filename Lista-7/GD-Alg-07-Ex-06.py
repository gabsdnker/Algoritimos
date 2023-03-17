#ANAGRAMAS NOVAMENTE

def anagramas(palavraA, palavraB):
    
    def conjuntos(palavra):
        conjunto = {""}
        for c in palavra:
            if c.isalpha() == True:                
                conjunto.add(c.upper())
        return(conjunto)
    A = conjuntos(palavraA)
    B = conjuntos(palavraB)    
    if A == B:
        anagrama = True
    else:
        anagrama = False  
    return(anagrama)

def main():
    palavra1 = input("Digite a primeira palavra: ")
    palavra2 = input("Digite a segunda palavra: ")
    resultado = anagramas(palavra1,palavra2)
    print(resultado)

if __name__ == '__main__':
    main()