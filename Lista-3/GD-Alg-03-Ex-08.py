#NOTA PARA FREQUÊNCIA

nota= input("Insira a nota: ")

c4= 261.63
d4= 293.66
e4= 329.63
f4= 349.23
g4= 392
a4= 440
b4= 493.88

x= int(nota[1])
print("Frequência: ")

if nota[0]== "C":
    print(c4/2**(4-x), "Hz")
elif nota[0]== "D":
    print(d4/2**(4-x), "Hz")
elif nota[0]== "E":
    print(e4/2**(4-x), "Hz")
elif nota[0]== "F":
    print(f4/2**(4-x), "Hz")
elif nota[0]== "G":
    print(g4/2**(4-x), "Hz")
elif nota[0]== "A":
    print(a4/2**(4-x), "Hz")
elif nota[0]== "B":
    print(b4/2**(4-x), "Hz")
else:
    print("Inválido")