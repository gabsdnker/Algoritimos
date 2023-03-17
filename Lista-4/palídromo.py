#PALÍNDROMO

while True:
    palavra = input("Digite a palavra:")
    if str(palavra) == str(palavra)[::-1] :
        print("Palíndromo")
    else:
        print("Não é Palíndromo")
