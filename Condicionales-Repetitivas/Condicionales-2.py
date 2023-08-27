# 3. Pedirle al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro
# mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día
# ingresado no es ninguno de esos, imprimir otro mensaje.

dia_semana= input("Ingrese un dia de la semana: ")

if dia_semana== "lunes":
    print("Es el primer dia de la semana")
elif dia_semana== "martes":
    print("Es el segundo dia de la semana")
elif dia_semana== "miercoles":
    print("Falta menos para que el viernes")
elif dia_semana== "jueves":
    print("Mañana ya es viernes")
elif dia_semana== "viernes":
    print("Ultimo dia de la semana")
elif dia_semana== "sabado" or dia_semana== "domingo":
    print("Es fin de semana")
else:
    print("No es un dia de la semana,vuelva a intentar")