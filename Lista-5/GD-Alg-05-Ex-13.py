#DIAS EM UM MêS

#QUANTOS DIAS TEM CADA MêS
#1º PARAMETRO: O MÊS COMO UM NÚMERO INTEIRO ENTRE 1 A 12
#2º PARAMTRO: O ANO COMO UM NÚMERO INTEIRO DE 4 DIGITOS 
#INCLUIR UM PROGRAMA PRINNCIPAL QUE LÊ O MêS E O ANO DO USUÁRIO E EXIBIR O NÚMERO DE DIAS DO MÊS

def dias( mes, ano):
  mes_31= [1,3,5,7,8,10,12]
  mes_30= [4,6,9,11]
  if mes in mes_31:
    return "31 dias"
  elif mes in mes_30:
    return "30 dias"
  else:
    if ano%400==0 or ano%4==0:
      return "29 dias"
    else:
      return "28 dias"

def main():
  while True:
    mes= int (input("Digite o mês: "))
    ano= int(input("Digite o ano: "))
    print("O TOTAL DO DIA NO MÊS É ", dias(mes,ano))

if __name__=='__main__':
    main()