#PERÍMETRO DE UM POLIGNO

x= int(input("Digite as coordenadas x de um ponto: "))
y= int(input("Digite as coordenadas y de um ponto: "))

d= 0
p=1

while True:
    p= 1+p
    x1= input("Digite a coordenada x de um ponto {p} (enter para sair): ")
    if not x1:
        break
    else:
        y1= int(input("Digite a coordenada y de um ponto {p} (enter para sair): "))
        distancia= d
        distancia= ((y1- y)**2+(int(x1)-x)**2)**(1/2)
        distancia= distancia+d
        x= int(x1)
        y=y1
        print("O perímetro é: ", distancia)