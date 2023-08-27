# 4. Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma y la
# media de todos los números introducidos.

suma = 0
contador = 0

while True:
    numero = float(input("Introduce un número (introduce 0 para terminar): "))
    
    if numero == 0:
        break
    
    suma += numero
    contador += 1

if contador > 0:
    media = suma / contador
else:
    media = 0

print(f"La suma de los números introducidos es: {suma}")
print(f"La media de los números introducidos es: {media}")
