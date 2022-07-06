#       Ejercio 3- desafio3_recordatorios 
#Desarrollado por: Elio Duran

""" 
Se provee del archivo recordatorios.py que incluye una serie de eventos
que quieren ser recordados por usted. El formato de estos recordatorios
son una fecha (año-mes-día), una hora y una descripción del evento.

Aplicando métodos apropiados para la estructura de datos entregada edite
la lista de recordatorios de la siguiente manera:
1. Agregue un evento el 2 de Febrero de 2021 a las 6 de la mañana para
“Empezar el Año”.
2. Al revisar los eventos, nota un error, ya que el 15 de Julio no es
feriado. Editar de tal manera que sea el 16 de Julio.
3. Lamentablemente le tocará trabajar el día del trabajo. Elimine el
evento del día del trabajo.
4. Agregue una cena de Navidad y de Año Nuevo cuando corresponda. Ambas
a las 22 hrs.
"""

path= "2.Fundamentos de la Programación y Estructuras de Datos/Taller/recordatorios.py"
with open(path, "r") as texto:
    texto =texto.read()

# Texto del archivo "recordatorios.py":
recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
    ['2021-05-01', "15:00", "No trabajar"],
    ['2021-07-15', "13:00", "No hacer nada, es feriado"],
    ['2021-09-18', "16:00", "Ramadas"],
    ['2021-12-25', "00:00", "Navidad"]]

#Ejecución de las nuevas necesidades:
print('Recordatorios = ')
recordatorios.insert(2,['2021-02-01', "06:00", "Empezar el Año"]) #Edición 1
recordatorios[3][0]='2021-07-16'  #Edición 2
recordatorios.pop(1) #Edición 3
recordatorios.insert(4, ['2021-12-24', '22:00', "Cena de Navidad"]) #Edición 4
recordatorios.append(['2021-12-31', '22:00', 'Cena de Año Nuevo']) #Edición 4
print(recordatorios)




