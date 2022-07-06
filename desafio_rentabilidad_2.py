# VERSION 2:

"""
Supongamos ahora que el emprendedor considera 2 tipos de usuarios diferenciados,
los usuarios normales y los usuarios premium a los cuales se les cobrará una
suscripción un 50% mayor. Crea una segunda versión llamada emprendedor2.py que
permita considerar el caso recién e50xpuesto. Para ello modifica la fórmula de
utilidades en la cual se solicite mediante input() los parámetros de entrada
precios de suscripción P, así como el número de usuarios Unormal y Upremium y
el gasto total GT. (3 Puntos)

"""
print('\nRequerimientos iniciales para el cálculo de las utilidades:\n')
print('NOTA: Recuerde solo ingresar números!!!\n')
numsuario1 = int(input('Ingrese el número de Ususarios Normales (Nota: usar solo numeros enteros):\n'))
numusuario2 = int(input('Ingrese el número de Ususarios Premium (Nota: usar solo numeros enteros):\n'))
precio=float(input('Ingrese el Precio de la Suscripción:\n'))
gastos= float(input('Ingrese los gastos totales:\n '))
utilidades=precio*(numsuario1 + 1.5*numusuario2)-gastos

print('\nSus Utilidades brutas serán:')
print(utilidades)
