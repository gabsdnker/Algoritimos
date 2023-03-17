#FIBINACCI COM MEMORIZAÇÃO DE RESULTADO

calculados = {0:0, 1:1, 2:1}
def fibonacci(n):
    if n in calculados:
        return calculados[n]
    resultado = (fibonacci(n-2) + fibonacci(n-1))
    calculados[n] = resultado
    return resultado

print(fibonacci(3))