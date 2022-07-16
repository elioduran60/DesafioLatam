    #           Módulo 11:
"""   
    Módulo 11 es un algoritmo con el cual se calcula el dígito verificador (o DV, 
    es el número que va después del guión) para los RUT en chile. Este número evita
    que cualquier persona pueda inventar un RUT aleatoriamente.
    Se pide crear un programa en Python llamado dv.py que permita ingresar el número
    de RUT sin puntos ni DV y devuelva el DV correspondiente.
    1. Se toma la siguiente serie numérica: 2, 3, 4, 5, 6, 7.
    2. Se multiplicará cada dígito del Número por su correspondiente en la serie numérica,
    partiendo desde el final del número. En caso de tener más números en la serie
    numérica, ésta se reinicia. 
    Finalmente se aplican las reglas del algoritmo:
        ○ Si el resultado es igual a 10, el DV es K
        ○ Si el resultado es 11, el DV es cero,
        ○ En cualquier otro caso, no se modifica.
"""

rut1=list(input('Ingrese el RUT sin puntos ni DV: '))#Entrada del número y conversión a lista\n",
serie=[2,3,4,5,6,7] # lista de referencia (ref.)

rut=[int(i) for i in rut1] # Convsersion de str a int cada elemento
rut.reverse() #Inversión de la lista para poder multiplicar con la lista de ref.\serie\

if len(rut) >= len(serie):
    for i in range(len(rut)-len(serie)):
        serie.append(i+2)
else:
    print('Revisar el númemro RUT ingresado')
suma=0
k='K'# NOTA: Este valor es constante en el sistema de identiifcacion chileno.
for i in range(len(rut)):
    suma=(rut[i] * serie[i]) + suma
dev=11-suma%11
if dev==10:
    print('Su dígito verificador es DV=',k)
elif dev==11:
    print('Su dígito verificador es DV:',0)
else:
    print('Su dígito verificador es DV=',dev)
