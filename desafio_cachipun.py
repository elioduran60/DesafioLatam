# Desafío - Cachipún
"""
Reuerimientos:
1. Se pide crear el programa cachipun.py, donde el usuario entregará como
argumento: piedra, papel o tijera. Para que el computador pueda jugar escogerá un
valor al azar. Para eso se solicita investigar random.choice() de la librería random.
(2 Puntos)

2. Considerar las opciones de ganar, perder o empatar con la computadora.
(5 Puntos)
3. En caso que el argumento sea distinto a piedra, papel o tijera, el programa debe
mostrar las opciones que se pueden jugar. (3 Puntos)
"""

# Solucion 1:

import sys
import random

# SOLUCION 1:
usuario=(sys.argv[1])

# SOLUCION 2:
# usuario=input('\nIngrese su palabra del juego(piedra, papel o tijera):')

usuario=usuario.lower()
computador=random.choice(['piedra','papel','tijera'])
jug_comput=str ('El Computador jugó:')
jug_usurio=str('Tu jugaste:')

if usuario !='piedra' and usuario !='papel' and usuario !='tijera':
    print('**-> Argumento ingresado es inválido!: Debe ser piedra, papel o tijera.')
else:
    if computador ==usuario:
        print(jug_comput, computador)
        print(jug_usurio, usuario)
        print('Hubo empate')
    elif computador =='papel' and (usuario=='piedra' or usuario== 'tijera'):
        print(jug_comput, computador)
        print(jug_usurio, usuario)
        print('Ganaste!!')
    elif (computador=='piedra' or computador== 'tijera') and usuario =='papel' :
            print(jug_comput, computador)
            print(jug_usurio, usuario)
            print('Perdiste!!')

