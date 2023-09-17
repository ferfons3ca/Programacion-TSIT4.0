#TUPLAS
#Crear tres tuplas con datos random
#Crear una lista que las contenga y mostrarla
import random

tupla1 = (random.randint(1, 100), random.choice(["frutas", "oceano", "plantas"]), random.uniform(1.0, 10.0))

tupla2 = (random.randint(1, 100), random.choice(["animal", "objeto", "pais"]), random.uniform(1.0, 10.0))

tupla3 = (random.randint(1, 100), random.choice(["color claro", "color oscuro"]), random.uniform(1.0, 10.0))


lista_de_tuplas = [tupla1, tupla2, tupla3]

print(lista_de_tuplas)
