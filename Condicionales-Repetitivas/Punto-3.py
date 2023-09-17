# 3. Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso
# contrario, el programa termina cuando se introduce un cero.
vocales= "aeiouAEIOU"
while True:
    entrada = input("Ingrese un caracter (o 0 para salir): ")

    if entrada == '0':
        break

    if len(entrada) == 1 and entrada.isalpha():
        caracter = entrada.lower()
        if caracter in vocales:
            print("VOCAL")
        else:
            print("NO VOCAL")
    else:
        print("inválido. Ingrese solo un caracter.")

print("Programa terminado.")
