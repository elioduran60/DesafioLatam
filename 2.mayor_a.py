#                   Filtrado compacto
"""
Se solicita devolver un informe resumido que exponga los meses que superan un 
cierto umbral. El programa "mayor_a.py" debe retornar un diccionario con el mes
y el valor asociado siempre y cuando superen el umbral especificado.
La empresa provee sus balances del año anterior en un diccionario como se 
muestra a continuación:
"""
ventas = {
"Enero": 15000,
"Febrero": 22000,
"Marzo": 12000,
"Abril": 17000,
"Mayo": 81000,
"Junio": 13000,
"Julio": 21000,
"Agosto": 41200,
"Septiembre": 25000,
"Octubre": 21500,
"Noviembre": 91000,
"Diciembre": 21000,
}

print('\n *******Programa de Filtrado compacto*******\n')
refer=float(input('Ingrese la cifra de referencia para obtener los meses que la superen:\n'))

filtrado={k:v for (k,v) in ventas.items() if v > refer }

print(filtrado)






