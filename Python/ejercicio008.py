"""
STRING y más!!!
"""
esto_es_una_string = "hola jose cordova como estas"
esto_es_otra_string = "Mundo"

#Concatenar
print (esto_es_una_string + ' ' + esto_es_otra_string)
# Hola mundo

#MAYUS
print (esto_es_una_string.upper())
#minus
print (esto_es_una_string.lower())
#Primera en mayúscula
print (esto_es_una_string.capitalize())
#Pone en mayúscula la primera letra de cada palabra
print (esto_es_una_string.title())
#Me dice la longitud del string
print (len(esto_es_una_string))

#buscar un carácter y muestra su ubicación
print (esto_es_una_string.find('e'))

#rebanar!!! o slice
#[inicio:fin:incremento]
print (esto_es_una_string [0:2]) #le digo que inicie en cero / ho
print (esto_es_una_string [:2]) #asume que inicia en cero / ho
print (esto_es_una_string [5:9])

#Radar
variable = 'jose'
print (variable [::])
print (variable [::-1])


