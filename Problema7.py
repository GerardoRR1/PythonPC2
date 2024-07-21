def es_num_perfect(n):
    suma_divisores = sum(i for i in range(1, n) if n % i == 0)
    return suma_divisores == n

numeros_perfectos = [n for n in range(1, 1000) if es_num_perfect(n)]

print(numeros_perfectos)
