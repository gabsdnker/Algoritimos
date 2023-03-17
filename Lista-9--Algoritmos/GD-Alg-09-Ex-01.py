#Passagem de argumentos para o programa em linha de comando.

#a) Escreva o seguinte código Python, que lê e exibe os argumentos passados em linha de comando

import sys
if __name__ == "__main__":
    print(f"Número de argumentos: {len(sys.argv)}")
for i, arg in enumerate(sys.argv):
    print(f"Argumento {i}: {arg}")

#b)Faça um teste de execução do seu programa em linha de comando. A imagem abaixo mostra um teste realizado pelo professor, passando argumentos a, b, e c com o seguinte comando:

#Número de argumentos: 4
#Argumento 0: GD-Alg-09-Ex-01.py
#Argumento 1: a
#Argumento 2: b
#Argumento 3: c