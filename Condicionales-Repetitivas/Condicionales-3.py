# 4. Escribir un programa que solicite al usuario una letra y, si es una vocal, muestre el mensaje “es vocal”.

def es_vocal(letra):
    vocales = "aeiouAEIOU"
    if letra in vocales:
        return True
    else:
        return False

letra = input("Ingrese una letra: ")

if len(letra) == 1 and letra.isalpha():
    if es_vocal(letra):
        print("Es una vocal")
    else:
        print("No es una vocal")
else:
    print("Por favor ingresar una letra valida")