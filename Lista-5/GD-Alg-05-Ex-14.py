#DATAS MÁGICAS

#É UMA DATA NA QUAL A MULTIPLICAÇÃO DO DIA PELO MÊS É IGUAL AOS DOIS ÚLTIMOS DÍGITOS DO ANO
#EXEMPLO: 10 DE JUNHO DE 1960 É UMA DATA MÁGICA PORQUE 10*6= 60 
#FUNÇÃO DEVE RECEBER 3 PARAMETROS (DIA, MÊS E ANO)
#ESCREVER UMA FUNÇÃO MAIN QUE UTILIZE SEU FUNÇÃO PARA DETERMINAR E IMPRIMIR TODAS AS DATAS MÁGICAS DO SÉCULO 20
def main():
    dia= int(input("digite o dia: "))
    mes= int(input("digite o mes: "))
    ano= int(input("digite o ano: "))
    data_mágica= dia*mes
    print("Dois ultimos números ",data_mágica, "do ano ",ano)
if __name__== '__main__':
    main()