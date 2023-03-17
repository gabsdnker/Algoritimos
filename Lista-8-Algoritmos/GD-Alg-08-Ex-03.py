#PALÍNDROMO

def palindromo(txt):
    return len(txt) <= 1 or (txt[0] == txt[-1] and palindromo(txt[1:-1]))

print(palindromo("arara"))