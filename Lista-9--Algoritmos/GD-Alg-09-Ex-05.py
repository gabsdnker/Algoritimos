#Numerar as linhas de um arquivo.

# O programa deve receber do usuário os nomes do arquivo de entrada e do arquivo de saída (que será um novo arquivo criado pelo programa).
#Cada linha do arquivo de saída deve começar com leu número, seguido de dois pontos, um espaço em branco, seguido do conteúdo da linha do arquivo original.

arquivo_entrada= input("Digite o nome do arquivo: ")
arquivo_saida= input("Digite o nome novo do arquivo: ")


with open(arquivo_entrada, 'r') as fonte, open(arquivo_saida, 'w') as destino: #cria o arquivo
   i=1 
   while b := fonte.readline(): #para ler o arquivo de entrada 
        destino.write(f"{i} {b}") #escrevendo no destino, númerando linhas e o que foi lido do arquivo fonte
        i+=1 
       