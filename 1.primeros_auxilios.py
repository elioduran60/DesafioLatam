#           Primeros Auxilios
"""
Se requiere la construcción de una aplicación interactiva primeros_auxilios.py que
entregue los distintos pasos a seguir dependiendo de las respuestas que el usuario
entrega en tiempo real.
"""
print('\n *******Pasos de PRIMEROS AUXILIOS para personas*******\n')
estimulos=input('Ingrese "Si" si el paciente responde a estimulos, "No" sino responde:\n ')
estimulos=estimulos.lower()
if estimulos=='si':
    print('\n--> Verificar la necesidad de llevar al paciente al Hospital mas cercano.\n ')
else:
    print('\n --> Abrir la via Aérea del paciente.\n ')
    respira=input('Ingrese "Si" si el paciente respira, o Ingrese "No" sino respira: \n ')
    estimulos=respira.lower()
    if respira=='si':
        print('--> Permitir posición de suficiente ventilación\n ')
    else:
        print('\n --> Administrar 5 ventilaciones y llamar a la Ambulancia\n ')
        print('\n Verificar la llegada de la Ambulancia.....\n')
        ambulancia=input('Ingrese "Si" si llegó la Ambulancia, o Ingrese "No" sino lo ha llegado:\n ')
        ambulancia=ambulancia.lower()
        while ambulancia =='no':
            seguro=input('Ingrese "Si" si el paciente posee Seguro de Vida, o Ingrese "No" sino lo tiene;\n ')
            seguro=seguro.lower()
            if seguro=='si':
                print('--> Revaluar a la espera de la Ambulancia.\n')
            else:
                print('--> Administrar Compresiones toráxicas hasta que llegue la Ambulancia.\n')
            ambulancia=input('Ingrese "Si" si llegó la Ambulancia, o Ingrese "No" sino lo ha llegado:\n ')
            ambulancia=ambulancia.lower()
        

