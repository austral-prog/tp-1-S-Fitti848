def grades():
    """
    Ejercicio 11 - Promedio de Calificaciones

    Dadas tres notas, calcular e imprimir:
    1. El promedio de las tres notas
    2. La nota máxima
    3. La nota mínima
    4. Cuántos puntos faltan del promedio a 10
    """
"""
    nota1 = 8
    nota2 = 7
    nota3 = 9
"""

nota1 = int(input("Ingrese la nota 1: "))
nota2 = int(input("Ingrese la nota 2: "))
nota3 = int(input("Ingrese la nota 3: "))
prom= ((nota1 + nota2 + nota3)/3)

print(prom)
print (max (nota1, nota2, nota3))
print (min (nota1, nota2, nota3))
print(10 - prom)