#       Ejercio 2- Desafio a Estrucutura de Datos
#Desarrollado por: Elio Duran
# PLANTEAMIENTO:
"""
Crear un archivo conversiones.py y una estructura de datos apropiada
que permita ingresar tasas de conversión. Las distintas tasas de 
conversión se deben ingresar mediante sys.argv en el siguiente orden:
Sol, Peso Argentino, Dólar Americano. 
Para ello considere las siguientes tasas de conversión de Peso Chileno:
    ● a Sol peruano: 0.0046
    ● a Peso Argentino: 0.093
    ● a Dólar Americano: 0.00013
Nota: ingrese un 4to argumento que sea el valor en peso chileno a
convertir. El programa debe devolver el valor en peso chileno 
convertido en las 3 divisas ingresadas.
"""
# SOLUCION:
#Variables conocidas: (Diccionario de Tabla de Conversión)
tabla_conver= { 'Soles peruanos':0.0046, 'Pesos argentinos': 0.093,
                'Dólares americanos': 0.0013 } 
# Ingreso de parametros:
p_chile=float(input('\nIngrese la cantidad de pesos chilenos a convertir:'))
clave=list(tabla_conver.keys()) #conversion de dict -> lista (nombre moneda)
valor=list(tabla_conver.values()) #conversion de dict -> lista (valor moneda)
#Conversiones de modendas
soles=valor[0]*p_chile
p_argent=valor[1]*p_chile
dolar=valor[2]*p_chile

#Impresion de resultados:
print(f'\nLos {p_chile} pesos ingresados equivalen a: ')
print(f' {soles:.1f} {clave[0]} ') 
print(f' {p_argent:.1f} {clave[1]}') 
print(f' {dolar:.1f} {clave[2]}\n') 





