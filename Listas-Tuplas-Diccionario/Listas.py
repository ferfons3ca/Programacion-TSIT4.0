#LISTAS
familia= ["luis", "fernanda", "alberto", "maria"]
familia2= ["exequiel","leonardo", "evelyn", "alejandra"]
familia3= ["axel", "mateo", "agustin", "luz"]
familia4= ["federico", "martin", "carolina", "cristina"]
print(f"{familia}\n{familia2}\n{familia3}\n{familia4}")
print("------------------------------------------------------------------------------------------------------------------------------------------------")


#Temperatura
Mes="TEMPERATURAS MES DE SEPTIEMBRE:"
Temp_Sep= [29.2, 26.8, 14.5, 30.9, 31.7, 28.1, 24.3, 30.5, 18.2, 29.8, 28.4, 28.0, 
                   23.9, 26.7, 25.9, 29.8, 30.2, 35.6, 28.4, 24.5, 27.8, 23.6, 25.1, 27.9, 
                   23.3, 29.7, 34.9, 30.3, 28.7, 26.6]
print(f"{Mes}\n{Temp_Sep}")
print("------------------------------------------------------------------------------------------------------------------------------------------------")

#Ciudades
ciudades_visitadas= ["buenos aires", "santa fe", "cordoba"]
ciudades_visitadas2= ["barcelona", "roma", "venecia"]
ciudades_visitadas3= ["los angeles","san francisco", "mexico"]
ciudades_visitadas4= ["tokio", "dubai", "rio de janeiro"]
print(f"{ciudades_visitadas}\n{ciudades_visitadas2}\n{ciudades_visitadas3}\n{ciudades_visitadas4}")
print("------------------------------------------------------------------------------------------------------------------------------------------------")

#Eventos
evento= ["nacimiento de mi hermana","(3-12-05)"]
evento2= ["nacimiento de mi hermano", "(5-9-11)"]
evento3= ["armado de mi pc gamer","22-2-23"]
evento4= ["mi primera moto", "13-3-24"]
print(f"{evento}\n{evento2}\n{evento3}\n{evento4}")
print("------------------------------------------------------------------------------------------------------------------------------------------------")

#Ordenar Alfabeticamente Nombres
ordenarfamilia= [familia,familia2,familia3,familia4]
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
quitarfamiliar= ["leonardo","alejandra","agustin","axel"]
quitarfamiliar.remove("maria")
quitarfamiliar.remove("fernanda")
print(quitarfamiliar)
print("------------------------------------------------------------------------------------------------------------------------------------------------")

#Quitar de la lista de ciudades la ciudad menos linda que hayas visitada
ciudades= [ciudades_visitadas,ciudades_visitadas2,ciudades_visitadas3,ciudades_visitadas4]
ciudades.remove(ciudades_visitadas2)
print(ciudades)
print("------------------------------------------------------------------------------------------------------------------------------------------------")

#Mostrar todas las listas
lista_de_listas = [[familia,familia2,familia3,familia4],[Temp_Sep],[ciudades_visitadas,ciudades_visitadas2,ciudades_visitadas3,ciudades_visitadas4],[evento,evento2,evento3,evento4],
                   [ordenarfamilia],[Temp_oct],[quitarfamiliar],[ciudades]]
print(lista_de_listas)
print("------------------------------------------------------------------------------------------------------------------------------------------------")