#TABELA DE MULTIPLICAÇÃO

print("\t", end=" ")
for coluna in range(1,11):
    print(coluna, "\t", end=" ")

print()
for linha in range(1,11):
    print(linha, "\t", end=" ")
    for coluna in range(1,11):
        print(linha*coluna, "\t", end=" ")
    print()