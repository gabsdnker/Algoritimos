#CENTRALIZANDO UMA STRING

def centralizando(s, l):
    largura= l//2
    string= " "
    e= largura * string
    return e+s+e

def main():
    palavra= input("Digite a palavra: ")
    comprimento= int(input("Digite a largura da palavra: "))
    c= centralizando(palavra, comprimento)
    print(c)

if __name__ == '__main__':
    main()
