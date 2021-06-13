#Programa que nos va a comprobar si una palabra es palíndromo

Palabra = input ("Por favor, ingrese una palabra para comprobar si es un palíndromo: ")

print (Palabra)
print (Palabra [::-1])

#Condición
if (Palabra == Palabra[::-1]):
    print ("La palabra ingresada si es un palíndromo")
else: 
    print ("La palabra ingresada no es un palíndromo")