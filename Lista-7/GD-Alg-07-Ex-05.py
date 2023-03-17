#ANAGRAMAS

def anagramas(palavraA, palavraB):
    conjuntoA = {""}
    conjuntoB = {""}
    for letra in palavraA:
        conjuntoA.add(letra)
    for letra in palavraB:
        conjuntoB.add(letra)
    if conjuntoB == conjuntoA:
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
