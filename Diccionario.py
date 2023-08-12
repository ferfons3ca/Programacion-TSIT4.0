#Crear el siguiente diccionario:
# Las claves serán los dni de su núcleo familiar, y el valor será SOLO el nombre de la persona.
# Luego deberán añadir los datos de familia ampliada (abuelos, familia política, etc)

nucleo_familiar= {
      14473565: {
            "nombre":"maria",
            "parentesco":"abuela"
      },
      28994556: {
            "nombre":"claudio",
            "parentesco":"primo"
      },
      36556448: {
            "nombre":"alejandra",
            "parentesco":"tia"
      },
      46345777: {
            "nombre":"leonardo",
            "parentesco":"tio"
      }}
print(nucleo_familiar)
print("------------------------------------------------------------------------------------------------------------------------------------------------")

#Crear un nuevo diccionario con claves autogeneradas y valores de números de teléfono.Ambos deben ser mostrados.
import random

nombres = ["leonardo", "maría", "claudio", "alejandra", "luis"]
diccionario_telefonos = {}

for nombre in nombres:
    numero_telefono = "".join([str(random.randint(0, 9)) for _ in range(9)])
    diccionario_telefonos[nombre] = numero_telefono
    
print("Diccionario de Teléfonos:")
for nombre, telefono in diccionario_telefonos.items():
    print(f"Nombre: {nombre} - Teléfono: {telefono}")
print("------------------------------------------------------------------------------------------------------------------------------------------------")
