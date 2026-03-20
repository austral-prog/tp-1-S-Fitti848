def statistics():
    """
    Ejercicio 5 - Estadísticas Simples

    Dados cuatro números, calcular e imprimir:
    1. El promedio
    2. El máximo
    3. El mínimo
    4. El rango (diferencia entre máximo y mínimo)
    """
    num1 = 15
    num2 = 8
    num3 = 23
    num4 = 12

num1=(int)(input("Ingrese un numero: "))
num2=(int)(input("Ingrese un numero: "))
num3=(int)(input("Ingrese un numero: "))
num4=(int)(input("Ingrese un numero: "))

promedio = (num1+num2+num3+num4)/4
max= max (num1,num2,num3,num4)
min= min (num1,num2,num3,num4)
rang = max -min

print("El promedio es: ", promedio)
print(max)
print(min)
print(rang)