def currency():
    """
    Ejercicio 13 - Conversión de Moneda

    Dado un monto en pesos argentinos y tasas de cambio, imprimir:
    1. El monto en dólares
    2. El monto en euros
    3. El monto en reales brasileños
    """
    pesos = 10000
    tasa_dolar = 1500
    tasa_euro = 1600
    tasa_real = 250

    print(pesos / tasa_dolar)
    print(pesos / tasa_euro)
    print(pesos / tasa_real)

currency()
