#MDC- MÁXIMO DIVISOR COMUM 

def mdc(a, b):  
    if b == 0:
        return a
    c = a%b
    return(mdc(b, c))

print(mdc(81,63))