
n = int(input("Ingrese la cantidad de alumnos a registrar: "))

alumnos = []

# Ingresar los datos de los alumnos
for i in range(1, n + 1):
    alumno = {} 
    
    nombre = input(f"Ingrese el nombre del alumno {i}: ")
    alumno['Alumno'] = nombre
    
    # Ingreso de las 3 calificaciones del alumno
    notas = []
    for j in range(3):
        calificacion = float(input(f"Ingrese la calificación {j+1} de {nombre}: "))
        notas.append(calificacion)
    
    alumno['Notas'] = notas
    
    # Agregar el diccionario del alumno a la lista de alumnos
    alumnos.append(alumno)

# Mostrar el listado completo de alumnos
print("\nListado completo de alumnos y calificaciones:\n")
for alumno in alumnos:
    print(f"Alumno: {alumno['Alumno']}")
    print(f"Notas: {alumno['Notas']}")
    print()