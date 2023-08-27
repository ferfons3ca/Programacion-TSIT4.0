#LISTAS

abuelo= "luis"
mamá= "fernanda"
papá= "alberto"
abuela= "maria"
print(f"{abuelo}\n{mamá}\n{papá}\n{abuela}")
print("------------------------------------------------------------------------------------------------------------------------------------------------")


#Temperatura
Mes="TEMPERATURAS MES DE SEPTIEMBRE:"
Temp_Sep= [29.2, 26.8, 14.5, 30.9, 31.7, 28.1, 24.3, 30.5, 18.2, 29.8, 28.4, 28.0, 
                   23.9, 26.7, 25.9, 29.8, 30.2, 35.6, 28.4, 24.5, 27.8, 23.6, 25.1, 27.9, 
                   23.3, 29.7, 34.9, 30.3, 28.7, 26.6]
print(f"{Mes}\n{Temp_Sep}")
print("------------------------------------------------------------------------------------------------------------------------------------------------")

#Ciudades
ciudad= "buenos aires"
ciudad2= "cordoba capital"
ciudad3= "santa fe"
ciudad4= "mendoza"
print(f"{ciudad}\n{ciudad2}\n{ciudad3}\n{ciudad4}")
print("------------------------------------------------------------------------------------------------------------------------------------------------")

#Eventos
evento= "nacimiento de mi hermana (3-12-05)"
evento2= "nacimiento de mi hermano (5-9-11)"
evento3= "armado de mi pc gamer (2021)"
evento4= "mi primera moto (2023)"
print(f"{evento}\n{evento2}\n{evento3}\n{evento4}")
print("------------------------------------------------------------------------------------------------------------------------------------------------")

#Ordenar Alfabeticamente Nombres
ordenarfamilia= [abuelo,mamá,papá,abuela]
ordenarfamilia.sort()
print(ordenarfamilia)
print("------------------------------------------------------------------------------------------------------------------------------------------------")

#Ordenar ascendentemente la lista de temperaturas
Temp_Sep=[29.2, 26.8, 14.5, 30.9, 31.7, 28.1, 24.3, 30.5, 18.2, 29.8, 28.4, 28.0, 
                   23.9, 26.7, 25.9, 29.8, 30.2, 35.6, 28.4, 24.5, 27.8, 23.6, 25.1, 27.9, 
                   23.3, 29.7, 34.9, 30.3, 28.7, 26.6]
Temp_Sep.sort()
print(Temp_Sep)
print("------------------------------------------------------------------------------------------------------------------------------------------------")

#Agregar en la lista de temperaturas, las temperaturas de los 15 días del mes siguiente
Temp_oct=[26.7, 25.9, 29.8, 30.2, 35.6, 28.4, 24.5,30.9, 31.7, 28.1, 24.3, 30.5, 18.2, 29.8,29.2]
print(Temp_Sep,Temp_oct)
print("------------------------------------------------------------------------------------------------------------------------------------------------")

#Quitar de la lista de los nombres de familia, a tus abuelos
quitarfamiliar= [abuela,mamá,papá,abuelo]
quitarfamiliar.remove(mamá)
quitarfamiliar.remove(papá)
print(quitarfamiliar)
print("------------------------------------------------------------------------------------------------------------------------------------------------")

#Quitar de la lista de ciudades la ciudad menos linda que hayas visitada
ciudades= [ciudad,ciudad2,ciudad3,ciudad4]
ciudades.remove(ciudad4)
print(ciudades)
print("------------------------------------------------------------------------------------------------------------------------------------------------")

#Mostrar todas las listas
lista_de_listas = [[abuelo,mamá,papá,abuela],[Temp_Sep],[ciudad,ciudad2,ciudad3,ciudad4],[evento,evento2,evento3,evento4],
                   [ordenarfamilia],[Temp_oct],[quitarfamiliar],[ciudades]]
print(lista_de_listas)
print("------------------------------------------------------------------------------------------------------------------------------------------------")