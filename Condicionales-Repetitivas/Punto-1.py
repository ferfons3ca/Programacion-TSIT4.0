# Ejercicios Estructuras Repetitivas:
# Resolver cada enunciado utilizando las estructuras FOR – WHILE, según usted crea
# correspondiente:

# 1. Escribir un programa que realice la sumatoria de los números que se quiera hasta ingresar
# hasta que se ingrese -1.


suma = 0
num = 0

while num != -1:
    num = int(input("Ingrese un número (-1 para terminar): "))
    suma += num

print("La sumatoria de los números ingresados es:", suma)