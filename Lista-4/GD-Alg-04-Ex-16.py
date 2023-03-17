#CARA OU COROA

import random
media= 0

for sorteios in range(1,11):
    numero= 0
    cara= 0 
    coroa= 0
    while cara != 3 and coroa != 3:
        sorteio= (random.randint(0,1))
        if sorteio== 1:
            print("A", end=" ")
            cara += 1
            coroa= 0
        elif sorteio == 0:
            print("0", end=" ")
            coroa+= 1
            cara= 0
        numero+= 1
    else:
        print(f"({numero} sorteios)")
    media+= numero

media = media/10
print(f"Na média, foram necessários {media} sorteios.")    