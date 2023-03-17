#Frequência de letras.

#Escreva um programa Python que faz a primeira parte deste processo, determinando e exibindo a frequência (percentual) de ocorrência de todas as letras em um arquivo.
#Ignore espaços, números e sinais de pontuação.
#Seu programa não deve diferenciar letras maiúsculas e minúsculas (portento deve tratar A e a como sendo a mesma letra).
#O usuário deve fornecer o nome do arquivo como argumento em linha de comando.

def frequencia_de_letras(arquivo):
    with open(arquivo, "r") as fonte:
        while x:=fonte.readline():
            lista = []
            for letra in x:
                a = letra.lower()
                if a.isalpha() == True:
                    lista.append(a)
                alfabeto = set(lista)

            dicionario = {}
            n = 0
            for letra in alfabeto:
                for item in lista:
                    if letra == item:
                        n += 1
                dicionario[letra] = ((n/len(lista)))
                n = 0
            lista1 = []
            for valor in sorted(dicionario, key = dicionario.get, reverse=True):
                lista1.append("{0:2}:{1:6.0%}".format(valor, dicionario[valor]))
            return lista
    
def main():
    arquivo = input("Arquivo: ")
    lista = (frequencia_de_letras(arquivo))            
    for item in lista:
        print(item)
    
if __name__ == "__main__":
    main()
