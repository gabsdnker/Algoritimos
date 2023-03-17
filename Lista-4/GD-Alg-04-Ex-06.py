#BITS PARIDADE

while True:
    bits= input( "DIGITE UM GRUPO DE 8 BITS: ")
    if not bits:
        break
    else:
        i= int(bits.count('1'))
        p= i%2
        if i%2 ==0:
            print(1)
            print(p)
            print(i)
        else:
            print(0)
            print(p)
            print(i)
else:
    erro != 8
    print("erro")