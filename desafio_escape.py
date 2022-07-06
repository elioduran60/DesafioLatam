# EJERCICIO 1:

"""
Se solicita crear un script escape.py que permita calcular la velocidad
de Escape ingresando como datos de entradas el radio r y la constante g.
Los datos de entrada deben ingresarse de manera interactiva utilizando
la función input(). (5 Puntos)
La formula de la velocidad de escape del planeta es: Ve= √2*g*r
"""

print('\nRequerimientos iniciales para el cálculo de la Velocidad de escape:\n')
print('NOTA: Recuerde solo ingresar números!!!\n')
r=float(input('Ingrese el Radio (r) del planeta en kilómetros:\n'))
g=float(input('Ingrese la Constante de Gravedad del planeta (g) en m/s**2 :\n'))
vk= (2*g*(r/1000))**0.5
ve= (2*g*(r*1000))**0.5
print(f'La Velocidad de Escape del planeta es: {(vk):.2f} [K/s]')
print(f'La Velocidad de Escape del planeta es: {(ve):.2f} [m/s]')


