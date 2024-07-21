def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1): #No se considera el 1 por ser un número simple
        if n % i == 0:
            return False
    return True

suma_primos = sum(n for n in range(2, 100) if es_primo(n))

print(suma_primos)