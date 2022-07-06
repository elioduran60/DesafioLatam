"""
Versión 1:¶
Crear el programa emprendedor1.py que utilice la fórmula descrita anteriormente
para calcular las utilidades de un proyecto.Para ello utiliza input() para 
solicitar como dato el precio de suscripción P, el número de usuarios U y el
gasto total GT. (5 Puntos)
"""
print('\nRequerimientos iniciales para el cálculo de las utilidades:\n')
print('NOTA: Recuerde solo ingresar números!!!\n')
numusuario = int(input('Ingrese el número de Ususarios (Nota: usar solo numeros enteros):\n'))
precio=float(input('Ingrese el Precio de la Suscripción:\n'))
gastos= float(input('Ingrese los gastos totales:\n '))
utilidades=precio*numusuario-gastos
print('\nSus Utilidades brutas serán:')
print(utilidades)
