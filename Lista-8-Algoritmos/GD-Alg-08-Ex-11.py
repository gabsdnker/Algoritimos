#CODIFICAÇÃO RUN-LENGHT

def run_lenght(texto):
    if len(texto) == 0 :
        return []
    i = 1
    while i != len(texto) and (texto[0 + i - 1] == texto[1 + i - 1]):
        i += 1 
    atual = [texto[0], i]
    return(atual + run_lenght(texto[i:])) 

def main():
    x = ["A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "B", "B", "B", "A", "A", "A", "A", "A", "A", "B"]
    print(run_lenght(x))

if __name__ == '__main__':
    main()