#ABAIXO E ACIMA DA MÉDIA

def media(notas):
    media_max= []
    media_min= []
    media_igual= []
    n= 1
    soma= 0

    for i in notas:
        soma+= i
        n += 1
    media1= soma/n

    for i in notas:
        if i > media1:
            media_max.append(i)
        elif i < media1:
            media_min.append(i)
        else:
            media_igual.append(i)
    return(media1, media_max, media_min, media_igual)

def main():
    notas=[]
    nota= input("Digite o valor da nota: ")
    while nota != "":
        notas.append(int(nota))
        nota = input("Digite o valor da nota: ")

    valormedio, maior, menor, igual= media(notas)
    print("O valor médio é ", valormedio)
    print("Os valores abaixo da média são ", menor)
    print("Os valores acima da meédia são ", maior)
    print("Os valores iguais a média são: ", igual)

if __name__== '__main__':
    main()