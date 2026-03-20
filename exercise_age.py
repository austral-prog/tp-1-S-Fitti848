""""
    Ejercicio 10 - Conversión de Edad a Tiempo

    Dada una edad en años, calcular e imprimir:
    1. La edad en meses (1 año = 12 meses)
    2. La edad en días (1 año = 365 días)
    3. La edad en horas (1 día = 24 horas)
    4. La edad en minutos (1 hora = 60 minutos)
    """
años= int(input("cuantos años tenes"))
meses=12
dias=365
horas=24
minutos=60

años2= (años * meses)
dias2= (años * dias)
horas2= (dias2 * horas)
minutos2= (horas2 * minutos)

print (años2)
print (dias2)
print (horas2)
print (minutos2)