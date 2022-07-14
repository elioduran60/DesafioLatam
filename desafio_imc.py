#                       Desafio IMC:
# Solucion 1:
#peso=float(input('\nIngrese el peso en Kilos:'))
#altura=float(input('Ingrese la talla altura en centrimetros:\n'))


# Solucion 2: (usando ARG)

#               SOLUCION 2: Usando la libriría Sys
import sys

peso=float((sys.argv[1])) 
altura=float((sys.argv[2]))
imc=peso/(altura/100)**2

if imc < 18.5:
    print('La clasificación OMS es: Bajo de Peso')
elif imc >= 18.5 and imc<25:
    print('La clasificación OMS es: Peso Adecuado')
elif imc >= 25 and imc<30:
    print('La clasificación OMS es: Sobrepeso')  
elif imc >= 30 and imc<35:
    print('La clasificación OMS es: Obesidad Grado I') 
elif imc >= 35 and imc<40:
    print('La clasificación OMS es: Obesidad Grado II') 
else:
    print('La clasificación OMS es: Obesidad Grado III') 
print(f'Su IMC es: {imc:.2f} Kg/m2 ')


