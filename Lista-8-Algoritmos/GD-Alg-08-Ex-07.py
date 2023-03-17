#Conversão decimal → binário iterativa.

def detector_bin_int(a):  
    binario = ""
    while a != 0:
        r = a%2
        binario = str(r) + binario
        a = a//2
    return(binario)

print(detector_bin_int(9))