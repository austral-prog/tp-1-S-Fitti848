def price():
    """
    Ejercicio 8 - Cálculo de Precio Final

    Dado un precio base, calcular e imprimir:
    1. El monto del impuesto (21%)
    2. El subtotal (precio base + impuesto)
    3. El monto de la propina (10% del subtotal)
    4. El precio final (subtotal + propina)
"""

"""""
precio_base = 100
"""

preciob= int(input("precio_base:"))

imp =(preciob * 21 )//100
subt =(preciob + imp )
propina =(subt * 10 )//100
final= (subt + propina)

print(imp)
print (subt)
print(propina)
print (final)
