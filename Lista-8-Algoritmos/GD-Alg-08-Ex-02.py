#SEQUENCIA DE FIBONACCI

def fibonacci(n):
    if n == 0:
        return 0
    elif n <= 2 and n != 0:
        return 1
    return (fibonacci(n-2) + fibonacci(n-1))

print(fibonacci(30))