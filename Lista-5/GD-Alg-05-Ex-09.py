#A STRING REPRESENTA UM INTEIRO?

#Função isInteger: Que determina se os caracteres em uma string representam ou não um inteiro válido
#Quando determinar se uma string representa um inteiro,você deve ignorar qualquer espaço em branco à esquerda ou à direita. 
#Uma vez que este espaço em branco é ignorado, uma string representa um inteiro se seu comprimento for pelo
#menos 1 e contiver apenas dígitos, ou se seu primeiro caractere for + ou - e o primeiro
#caractere é seguido por um ou mais caracteres, todos os quais são dígitos.
#métodos lstrip, rstrip e/ou strip do tipo de dados string.

def num_inteiro (x):
    nova_string= ""
    if x[0]== "+" or x[0]=="-":
       x= x[1:]
    for c in x:
        if c == " ":
            c= ""
       
        else:
            nova_string= nova_string + c
        return nova_string.isdigit()

    type (nova_string) is int  
    y= nova_string.isalnum()
    return y

def main():
    string= input("Digite uma string: ")
    print(num_inteiro(string))

if __name__ == '__main__':
    main()