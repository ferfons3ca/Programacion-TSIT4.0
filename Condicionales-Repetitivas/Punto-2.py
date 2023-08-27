# 2. Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a
# introducir). El programa debe informar de cuantos números introducidos son mayores que
# 0, menores que 0 e iguales a 0.


def main():
    cantidad_numeros = int(input("Introduce la cantidad de números a ingresar: "))
    numeros_mayores = 0
    numeros_menores = 0
    numeros_iguales = 0
    
    for _ in range(cantidad_numeros):
        numero = float(input("Introduce un número: "))
        if numero > 0:
            numeros_mayores += 1
        elif numero < 0:
            numeros_menores += 1
        else:
            numeros_iguales += 1
    
    print("Cantidad de números mayores que 0:", numeros_mayores)
    print("Cantidad de números menores que 0:", numeros_menores)
    print("Cantidad de números iguales a 0:", numeros_iguales)

if __name__ == "__main__":
    main()
