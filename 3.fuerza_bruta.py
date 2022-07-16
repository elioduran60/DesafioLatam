# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 20:44:06 2022

@author: DesafioLatam.com
Solucion de Elio Duran
"""


#                            Fuerza bruta
"""
Mediante el siguiente desafío se busca utilizar un algoritmo muy sencillo, llamado
fuerza bruta para determinar cuántos intentos son necesarios para encontrar combinaciones
numéricas en minúscula.
Para ello se ingresará un password oculto. Este password puede contener sólo
combinaciones de letras y se requiere determinar su seguridad. Un mayor número de
intentos implica un password más seguro:
El programa fuerza_bruta.py debe intentar todas las combinaciones de letras posibles,
en orden alfabético, hasta que la combinación de letras sea igual a la de la contraseña
indicada. Deberá hacer este proceso letra por letra, de izquierda a derecha.
Consideraciones
    ● Utilizar from string import ascii_lowercase
    ○ ascii_lowercase es un string con todas las letras del abecedario en
    minúsculas (sin la ñ).
    ● No considerar la ñ.
    ● Considera mayúsculas y minúsculas como una misma letra.
    ● Se considera "intento" cada vez que se compara una letra.
"""

from string import ascii_lowercase

print('\n *******Programa "Fuerza bruta" *******\n')

password1=input('Ingrese un password con solo letras: ')
password1=list(password1.lower())
if 'ñ' in password1:
    print('Password ingresado contiene caracteres NO válidos')
else:
#Filtrado del string entrante (eliminará cualquier numero y/o la letra "ñ")
    password =[(password1[i]) for i in range(len(password1)) if password1[i] in ascii_lowercase ] 
    if password!=password1: # Comparacion de las 2 listas para descartar valores numericos
        print('Password ingresado contiene caracteres NO válidos')
    else:
        aux=[]
        n=0
        for i in range(len(password)): #Iteracines para comparar cada letra de la contraseña
            for k in range(i+1):
                if password==aux: # Comparaciones de las 2 listas
                    n +=1 # contador de intentos
                    break
                else:
                    aux.append(password[k]) # Incializacion de la lista auxiliar con la 1ra letra del password
                    n += 1 # contador de intentos
        print(f'La contraseña fue forzada en {n} intentos' )