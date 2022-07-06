# VERSION 3:
"""
Considera ahora una tercera versión llamada emprendedor3.py utilizando
la fórmula original de utilidades donde el usuario ingrese el precio de
suscripción P, el número de usuarios normales U y los gastos GT. 
Adicionalmente, solicita las utilidades del año anterior, todo esto 
mediante input(). El programa debe calcular las utilidades actuales
y mostrar la razón entre las utilidades actuales y las del año anterior
con dos decimales. (2 Puntos)
"""

print('\nRequerimientos iniciales para el cálculo de las utilidades:\n')
print('NOTA: Recuerde solo ingresar números!!!\n')
numusuario = int(input('Ingrese el número de Ususario (Nota: usar solo numeros enteros):\n'))
precio=float(input('Ingrese el Precio de la Suscripción:\n'))
gastos= float(input('Ingrese los gastos totales:\n '))
utilidades=precio*numusuario-gastos
utlianterior = float(input('Ingrese las utilidades del año anterior:\n'))
razon=utilidades/utlianterior
print('\nSus Utilidades brutas::') 
print('Utilidades del año pasado:',utlianterior)
print('Utilidades actuales son:',utilidades)
print(f'Razon entre las dos Utilidades:{(razon):.2f}')
