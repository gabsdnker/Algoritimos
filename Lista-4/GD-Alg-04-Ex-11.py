#PALÍDROMOS COM MÚLTIPLAS PALAVRAS 

while True:
    frase = input("Digite uma frase/palavra: ").lower().strip().replace(' ', '')
    if frase == frase[::-1]:
        print('É palíndromo')
    else:
        print("Não é palíndromo")