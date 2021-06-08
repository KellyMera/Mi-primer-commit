# Ingresar un número e indicicar si es par o impar
"""dotstring
1. Pedir al usuario ingresar un número
2. Hacer el cálculo para ver si es par o impar (variable % 2 == 0 es par)
3. mostrar el mensaje
"""
num = int (input("Por favor, ingrese un número: "))

if (num == 0): #si el número es igual a cero
    print ("Cero")
elif (num % 2 == 0): #caso contrario si el número mod 2 es cero
    print ("El número que ingreso es par")
else: #caso contrario
    print ("El número que ingreso es impar")
