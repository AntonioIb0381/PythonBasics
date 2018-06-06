# -*- coding: utf-8 -*-
# Esto es un comentario magico, que no sera ignorado

"""
Esto es el here-doc
"""

'''
Esto tambien es un comentario here-doc
'''
# tambien pueden ser cadenas de caracteres
mensaje = '''
esto ya no es un comentario
esto tampoco, es una cadena de caracteres
'''

# cadenas de caracteres

nombre = "Antonio"
apellido = 'Ibarra' #Esta es la preferida

#concatenacion de cadenas

NombreCompleto = nombre + ' ' + apellido #entre comillas espacio blanco

print(NombreCompleto)

print(len(nombre)) #variable length

# transformacion a mayusculas

print(nombre.upper())
print(nombre.lower())
print(nombre.replace('o', 'x'))

# Funcion

print('hola antonio')

# Formateo de cadenas

MensajeDeSaludo = 'Hola soy %s' %nombre  # %s operador para cadenas
print(MensajeDeSaludo)


NombreDado = input("dime tu nombre: ") # raw_input no inerpreta el tipo de variable
print('tu nombre tiene %s caracteres' %len(NombreDado))

# otra forma
LongitudNombre = len(NombreDado)

print('tu nombre tiene: %s caracteres' %LongitudNombre)
