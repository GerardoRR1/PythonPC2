def factorial(n):
    if n < 0:
        raise ValueError("El número debe ser un entero no negativo")
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

numero = 4
print(f"El factorial de {numero} es {factorial(numero)}")