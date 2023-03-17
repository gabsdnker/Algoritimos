#TOTAL DE VALORES NÚMERICOS

n = 0
def soma(n):  
    m = n  
    n = input("Digite um número: ")
    if n == "":
        return float(0)
    total = int(n) + soma(m)
    return(total)

print(soma(n))