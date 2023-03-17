#CÓDIGO MORSE

def código_morse(texto):
    texto_morse = ""
    morse = {"A":".-", "B":"-...", "C":"-.-.", "D":"-..", "E":".", "F":"..-.", "G":"--.", "H":"....", "I":"..", "J":".---", "K":"-.-", "L":".-..", "M":"--", "N":"-.", "O":"---", "P":".--.", "Q":"--.-", "R":".-.", "S":"...", "T":"-", "U":"..-", "V":"...-", "W":".--", "X":"-..-", "Y":"-.--", "Z":"--..", "0":"-----", "1":".----", "2":"..---", "3":"...--", "4":"....-", "5":".....", "6":"-....", "7":"--...", "8":"---..", "9":"----.",}
    for c in texto:
        if c.isalpha() == True:
            d = morse[c.upper()]
            texto_morse = texto_morse + d + " "
        elif c.isnumeric() == True:
            d = morse[c]
            texto_morse += d + " "

    return(texto_morse)

def main():
    frase = input("Digite uma frase: ")
    x = código_morse(frase)
    print(x)

if __name__ == '__main__':
    main()