#Conversão decimal → binário recursiva.

def detector_bin_rec(a):  
    if a <= 1:
        return(a)
    r = a%2    
    binario = str(detector_bin_rec(a//2)) + str(r)
    return(binario)

def main():
    n = int(input("Digite um número inteiro positivo: "))
    if n < 0:
        print("Erro! O número deve ser positivo")
    print(detector_bin_rec(n))

if __name__ == '__main__':
    main()