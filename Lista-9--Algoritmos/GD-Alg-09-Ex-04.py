#CONCATENAR MÚTIPLOS ARQUIVOS 

#Escreva um programa Python que apresente o mesmo comportamento.
#O programa deve exibir uma mensagem de erro caso algum arquivo não puder ser lido, e então passa para a leitura do próximo arquivo.
#O programa também deve exibir mensagem de erro caso não tenha sido passado nenhum argumento para o programa em linha de comando.

with open("aternados.txt", "w") as file:
    for temp in ["Palavras_português_br-utf8.txt", "Palavra_portugues_br-utf16.txt"]:
        with open(temp, "r")  as t:
            file.writelines(t)

            
