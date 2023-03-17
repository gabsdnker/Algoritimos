#AVALIAÇÃO DE EXPRESSÃO PÓS-FIXADA

from collections import deque
 
# Função para avaliar uma dada expressão postfix
def evalPostfix(exp):
 
    # caso básico
    if not exp:
        exit(-1)
 
    # cria uma Stack vazia
    stack = deque()
 
    # percorre a expressão dada
    for ch in exp:
 
        # se a corrente for um operando, empurre-o para a Stack
        if ch.isdigit():
            stack.append(int(ch))
 
        # se a corrente for um operador
        else:
            # remove os dois primeiros elementos da Stack
            x = stack.pop()
            y = stack.pop()
 
            # avalia a expressão 'x op y' e pressiona o botão
            # Resultado # de volta à Stack
            if ch == '+':
                stack.append(y + x)
            elif ch == '-':
                stack.append(y - x)
            elif ch == '*':
                stack.append(y * x)
            elif ch == '/':
                stack.append(y // x)
 
    # Neste ponto, a Stack fica com apenas um elemento, ou seja,
    # resultado da expressão de
    return stack.pop()
 
if __name__ == '__main__':
 
    exp = input("Digite uma pós-fixa: ")
    print(evalPostfix(exp))