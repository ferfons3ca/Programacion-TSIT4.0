#LISTAS

familia= " fernanda,paulina,luis,bautista,maria,alberto"
print(familia)
print("------------------------------------------------------------------------------------------------------------------------------------------------")


#Temperatura
Mes="TEMPERATURAS MES DE SEPTIEMBRE:"
Temperatura_Septiembre= [29.2, 26.8, 14.5, 30.9, 31.7, 28.1, 24.3, 30.5, 18.2, 29.8, 28.4, 28.0, 
                   23.9, 26.7, 25.9, 29.8, 30.2, 35.6, 28.4, 24.5, 27.8, 23.6, 25.1, 27.9, 
                   23.3, 29.7, 34.9, 30.3, 28.7, 26.6]
print(f"{Mes}\n{Temperatura_Septiembre}")
print("------------------------------------------------------------------------------------------------------------------------------------------------")

#Ciudades
ciudadesvisitadas= [" Buenos Aires","Cordoba Capital","Santa Fe"]
print(ciudadesvisitadas)
print("------------------------------------------------------------------------------------------------------------------------------------------------")

#Eventos
eventos= "nacimiento de mis hermanos:\n paulina 3 de diciembre 2005\n bautista 5 de septiembre 2011"
print(eventos)
print("------------------------------------------------------------------------------------------------------------------------------------------------")

#Ordenar Alfabeticamente Nombres
ordenarfamilia= ["fernanda","paulina","luis","bautista","maria","alberto"]
ordenarfamilia.sort()
print(ordenarfamilia)
print("------------------------------------------------------------------------------------------------------------------------------------------------")

#Ordenar ascendentemente la lista de temperaturas
Temperatura_Septiembre=[29.2, 26.8, 14.5, 30.9, 31.7, 28.1, 24.3, 30.5, 18.2, 29.8, 28.4, 28.0, 
                   23.9, 26.7, 25.9, 29.8, 30.2, 35.6, 28.4, 24.5, 27.8, 23.6, 25.1, 27.9, 
                   23.3, 29.7, 34.9, 30.3, 28.7, 26.6]
Temperatura_Septiembre.sort()
print(Temperatura_Septiembre)
print("------------------------------------------------------------------------------------------------------------------------------------------------")

#Agregar en la lista de temperaturas, las temperaturas de los 15 días del mes siguiente
Temperatura_octubre=[26.7, 25.9, 29.8, 30.2, 35.6, 28.4, 24.5,30.9, 31.7, 28.1, 24.3, 30.5, 18.2, 29.8,29.2]
print(Temperatura_Septiembre,Temperatura_octubre)
print("------------------------------------------------------------------------------------------------------------------------------------------------")

#Quitar de la lista de los nombres de familia, a tus abuelos
quitarfamiliar= ["fernanda","paulina","luis","bautista","maria","alberto"]
quitarfamiliar.remove("maria")
quitarfamiliar.remove("luis")
print(quitarfamiliar)
print("------------------------------------------------------------------------------------------------------------------------------------------------")

#Quitar de la lista de ciudades la ciudad menos linda que hayas visitada
ciudades= [" Buenos Aires","Cordoba Capital","Santa Fe"]
ciudades.remove("Santa Fe")
print(ciudadesvisitadas)
print("------------------------------------------------------------------------------------------------------------------------------------------------")

#Mostrar todas las listas
print(familia,Temperatura_Septiembre,
      ciudadesvisitadas,eventos,ordenarfamilia,
      Temperatura_Septiembre,Temperatura_octubre,
      quitarfamiliar,ciudades)
print("------------------------------------------------------------------------------------------------------------------------------------------------")