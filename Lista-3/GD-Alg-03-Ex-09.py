#DATA DE FERIADO

dia= int(input("Insira o dia: "))
mes= int(input("Insira o mês: "))

if (dia== 1) and (mes== 1):
    print("Hoje é Confraternização Universal")
elif (dia== 21) and (mes== 4):
    print("Hoje é Tiradentes")
elif (dia== 1) and (mes== 5):
    print("Hoje é Dia do trabalho")
elif (dia== 7) and (mes== 7):
    print("Hoje é da Indepedência do Brasil")
elif (dia== 12) and (mes== 10):
    print("Hoje é dia da Nossa senhora Aparecida")
elif (dia== 2) and (mes== 11):
    print("Hoje é dia de Finados")
elif (dia== 15) and (mes== 11):
    print("Hoje é dia da Proclamação da República")
elif (dia== 25) and (mes== 12):
    print("Hoje é Natal")
else:
    print("Hoje não é feriado nacional brasileiro")