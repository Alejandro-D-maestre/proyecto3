# Lista con 5 notas de estudiantes
notas = [2.8, 3.5, 4.0, 2.9, 3.2]

# Calcular el promedio
promedio = sum(notas) / len(notas)

# Mostrar si el promedio es aprobado o reprobado
if promedio >= 3.0:
    print("Promedio:", promedio, "- Aprobado")
else:
    print("Promedio:", promedio, "- Reprobado")

# Mostrar las notas ordenadas de menor a mayor
notas_ordenadas = sorted(notas)
print("Notas ordenadas:", notas_ordenadas)