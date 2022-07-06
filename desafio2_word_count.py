#       Ejercio 2- desafio2_word_count
#Desarrollado por: Elio Duran

"""
El texto lorem ipsum es un texto de prueba que se utiliza para demostrar
distintas tipografías además de usarse para rellenar espacios que requieran
largos textos. ¿Cuántas palabras componen este texto? 
Genere un archivo llamado word_count.py que importe un texto a Python y 
realice las siguientes tareas:
● Utilizando una estructura de datos apropiada, cuente la cantidad 
de caracteres distintos que componen un texto.
● Cuente el número de palabras distintas que componen el texto ingresado.
Para separar un texto por espacios puede utilizar el método .split("").
"""
#Ubicacion del archivo (ruta):
path= "2.Fundamentos de la Programación y Estructuras de Datos/Taller/lorem_ipsum.txt"

with open(path,"r") as file:
    texto=file.read()

texto1=set(texto) # conversión de str a conjunto (set)
cart_dist=len(texto1) # conteo de catarteres distintos
texto2=set(texto.split()) # conversión de str a conjunto (set) y 
                        # separación de espacios y textos
pal_dist=len(texto2)  # conteo de palabrass distintos

print('El número de caracteres distintos es:',cart_dist)
print('El número de palabras distintas es:',pal_dist)



