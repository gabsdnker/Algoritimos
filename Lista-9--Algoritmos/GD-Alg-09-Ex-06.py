#Encontrar a palavra mais longa de um arquivo.

#Neste exercício você deve desenvolver um programa Python para identificar a(s) palavra(s) mais longa(s) de um arquivo.
#Seu programa deve exibir uma mensagem que inclua o tamanho da palavra mais longa, juntamente com todas as palavras daquele tamanho que existem no arquivo.
#Trate cada grupo de caracteres sem espaço como uma palavra, mesmo se esse grupo contiver números ou sinais de pontuação.

maior_palavra= 0

with open("bla.txt", 'r') as fonte:
    palavra= ""
    lista=[]
    while x:= fonte.readline():
        for letra in x: #ler arquivo
            if letra != " " and letra != "\n": 
                palavra= palavra + letra #aumenta palavra até completar 
         
                if len(palavra) > maior_palavra: 
                    maior_palavra= len(palavra)
                    lista.clear()
                    lista.append(palavra)
                elif len(palavra) == maior_palavra:
                    lista.append(palavra)
            else:
                palavra= ""
    print(lista, maior_palavra)
