def time():
    """
    Ejercicio 4 - Calculadora de Tiempo

    Dado un total de segundos, calcular e imprimir:
    1. Horas completas
    2. Minutos completos restantes
    3. Segundos restantes
    """
    seg = 3665

    hor = seg // 3600
    min = (seg % 3600) // 60
    seg2 = seg % 60

    print(hor)
    print(min)
    print(seg2)

time()
