#TARIFA DO TAXI

#VALOR INICIAL 4,00 REAIS 
#A CADA 140m AUMENTA 0,25 REAIS

def valor(x):
    valor_inicial= 4
    aumento= 0.25
    metros= 140
    x_metros= x*1000
    valor_final= valor_inicial+(x_metros//metros)*aumento
    return (valor_final)

def main():
    d=float(input("Quilômetros percorridos: "))
    print("R$",valor(d))

if __name__== '__main__':
    main()
