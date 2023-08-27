#Ejercicios Estructuras Condicionales:
#Resolver cada enunciado utilizando las estructuras IF – ELSE – ELIF, según usted crea
#correspondiente:
#1. Pedirle al usuario que ingrese un número, si este es 10 se debe imprimir: ¡Usted ha ganado el sorteo!
#2. Sumar al ejercicio anterior, una pregunta: Si el número es menor imprimir: ¡Falto un poco,
# seguí participando! Si es mayor, imprimir: ¡Te pasaste, a seguir intentando!

numero = int(input("Ingrese un número: "))

if numero== 10:
    print("¡Usted ha ganado el sorteo!")
elif numero< 10:
    print("¡Falto un poco,seguí participando!")
else:
    print("¡Te pasaste, a seguir intentando!")