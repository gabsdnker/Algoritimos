#VERIFICAÇÃO DE SENHA VALIDA

#CONTER PELO MENOS 8 CARACTERES A SENHA
#PELO MENOS UMA LETRA MAIUSCULA 
#PELO MENOS UMA LETRA MINUSCULA
#PELO MENOS UM NÚMERO
#RETORNAR TRUE OU FALSE

def senha (x):
    letra_maiuscula= 0
    letra_minuscula= 0
    numero= 0 
    if (len(x)>= 8):
        for i in x:
            if(i.islower()):
                letra_minuscula +=1
            elif (i.isupper()):
                letra_maiuscula +=1
            elif (i.isdigit()):
                numero +=1
    if (letra_minuscula>= 1 and letra_maiuscula>= 1 and numero>= 1 and letra_minuscula+letra_maiuscula+numero== len(x)):
        return True
    else:
        return False

def main ():
    print("SUA SENHA PRECISA DE LETRAS MAIUSCULAS, MINUSCULAS E NÚMEROS")
    s= input("Digite sua senha(pelo 8 caracteres): ")
    print(senha(s))

if __name__=='__main__':
    main()