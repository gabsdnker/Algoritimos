#UNIDADE DE TEMPO

dias= int(input("Digite a quantidade de dias: "))
horas= int(input("Digite a quantidade de horas: "))
minutos= int(input("Digite a quantidade de minutos: "))
segundos= int(input("Digite a quantidade de segundos: "))

dias= dias**24*60*60
horas= horas*60*60
minutos= minutos*60

t= dias+horas+minutos+segundos 
print("A quantidade de tempo em segundos: ", t)