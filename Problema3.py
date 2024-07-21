#Problema 3:

print('Bienvenido')

numeros_pares = 0
numeros_impares = 0
numeros_ingresados = []
while True:
    print("Desea ingresar un número? 1) SI 2) NO ")
    respuesta = input().strip().lower()
    if respuesta == 'si':
        numero = int(input("Ingrese un número: "))
        numeros_ingresados.append(numero)
        if numero % 2 == 0:
            numeros_pares += 1
        else:
            numeros_impares += 1
    elif respuesta == 'no':
        break
    else:
        print('Ingrese un valor válido')
print("Números ingresados:", numeros_ingresados)
print(f"Números pares: {numeros_pares}")
print(f"Números impares: {numeros_impares}")