

notas = []

#leer datos:
for x in range(3):
    nota = float(input(f"Ingrese la nota {x + 1}: "))  # Convertir la entrada a float
    notas.append(nota)

# Calcular el promedio
    promedio = sum(notas) / len(notas)

# Determinar si está aprobado o reprobado
if promedio > 1.7:
    estado = "aprobado"
else:
    estado = "reprobado"

# Imprimir resultados
print(f"El promedio es: {promedio:.2f}")
print(f"Estado: {estado}")