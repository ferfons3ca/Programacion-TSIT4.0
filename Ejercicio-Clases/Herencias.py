from enum import Enum

class Cursos:
    def __init__(self, fecha_comienzo, titulo, descripcion, objetivos, programa, costo, duracion_meses, foto, estado):
        self.fecha_comienzo = fecha_comienzo
        self.titulo = titulo
        self.descripcion = descripcion
        self.objetivos = objetivos
        self.programa = programa
        self.costo = costo
        self.duracion_meses = duracion_meses
        self.foto = foto
        self.estado = estado


    def get_descripcion(self):
        return self.descripcion

    def set_descripcion(self, descripcion):
        self.descripcion = descripcion

    def get_objetivos(self):
        return self.objetivos

    def set_objetivos(self, objetivos):
        self.objetivos = objetivos

    def get_programa(self):
        return self.programa

    def set_programa(self, programa):
        self.programa = programa

    def get_costo(self):
        return self.costo

    def set_costo(self, costo):
        self.costo = costo

    def get_duracion_meses(self):
        return self.duracion_meses

    def set_duracion_meses(self, duracion_meses):
        self.duracion_meses = duracion_meses

    def get_foto(self):
        return self.foto

    def set_foto(self, foto):
        self.foto = foto

    def get_estado(self):
        return self.estado

    def set_estado(self, estado):
        self.estado = estado
        
        
class Categoria:
    def __init__(self, inicial, intermedio, avanzado):
        self.inicial = inicial
        self.intermedio = intermedio
        self.avanzado = avanzado
        
    def get_inicial(self):
        return self.inicial
    
    def set_inicial(self,inicial):
        self.inicial=inicial
        
    def get_intermedio(self):
        return self.intermedio
    
    def set_intermedio(self,intermedio):
        self.intermedio=intermedio
        
    def get_avanzado(self):
        return self.avanzado
    
    def set_avanzado(self,avanzado):
        self.avanzado=avanzado
        
        
class Clases:
    def __init__(self, fecha, titulo, contenido, URLDrive):
        self.fecha = fecha
        self.titulo = titulo
        self.contenido = contenido
        self.URLDrive = URLDrive
        
    def get_fecha(self):
        return self.fecha
    
    def set_fecha(self,fecha):
        self.fecha=fecha
        
    def get_titulo(self):
        return self.titulo
    
    def set_titulo(self,titulo):
        self.titulo=titulo
        
    def get_contenido(self):
        return self.contenido
    
    def set_contenido(self,contenido):
        self.contenido=contenido
        
    def get_URLDrive(self):
        return self.URLDrive
    
    def set_URLDrive(self,URLDrive):
        self.URLDrive=URLDrive
        
              
class Usuario:
    def __init__(self, apellido, nombre, dni, fecha_nacimiento, direccion, localidad, codigo_postal, provincia, telefono_celular, email, rol):
        self.apellido = apellido
        self.nombre = nombre
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
        self.direccion = direccion
        self.localidad = localidad
        self.codigo_postal = codigo_postal
        self.provincia = provincia
        self.telefono_celular = telefono_celular
        self.email = email
        self.rol="alumno"
        self.estado="activo"
        

    def get_apellido(self):
        return self.apellido

    def set_apellido(self, apellido):
        self.apellido = apellido

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_dni(self):
        return self.dni

    def set_dni(self, dni):
        self.dni = dni
        
    def get_fecha_nacimiento(self):
        return self.fecha_nacimiento
    
    def set_fecha_nacimiento(self,fecha_nacimiento):
        self.fecha_nacimiento=fecha_nacimiento
        
    def get_codigo_postal(self):
        return self.codigo_postal
    
    def set_codigo_postal(self,codigo_postal):
        self.codigo_postal=codigo_postal
        
    def get_provincia(self):
        return self.provincia
    
    def set_provincia(self,provincia):
        self.provincia=provincia
        
    def get_telefono_celular(self):
        return self.telefono_celular
    
    def set_telefono_celular(self,telefono_celular):
        self.telefono_celular=telefono_celular
        
    def get_email(self):
        return self.email
    
    def set_email(self,email):
        self.email=email
        
    def get_rol(self):
        return self.rol
    
    def set_rol(self,rol):
        self.rol=rol
        
class Docentes(Usuario):
    def __init__(self, apellido, nombre, dni, fecha_nacimiento, direccion, localidad, codigo_postal, provincia, telefono_celular, email):
        super().__init__(apellido, nombre, dni, fecha_nacimiento, direccion, localidad, codigo_postal, provincia, telefono_celular, email)
    
        
    def get_apellido(self):
        return self.apellido

    def set_apellido(self, apellido):
        self.apellido = apellido

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_dni(self):
        return self.dni

    def set_dni(self, dni):
        self.dni = dni
        
    def get_fecha_nacimiento(self):
        return self.fecha_nacimiento
    
    def set_fecha_nacimiento(self,fecha_nacimiento):
        self.fecha_nacimiento=fecha_nacimiento
        
    def get_codigo_postal(self):
        return self.codigo_postal
    
    def set_codigo_postal(self,codigo_postal):
        self.codigo_postal=codigo_postal
        
    def get_provincia(self):
        return self.provincia
    
    def set_provincia(self,provincia):
        self.provincia=provincia
        
    def get_telefono_celular(self):
        return self.telefono_celular
    
    def set_telefono_celular(self,telefono_celular):
        self.telefono_celular=telefono_celular
        
    def get_email(self):
        return self.email
    
    def set_email(self,email):
        self.email=email
        

def crear_cuenta():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    dni = input("DNI: ")
    direccion = input("Dirección: ")
    fecha_nacimiento = input("Fecha de Nacimiento: ")
    localidad = input("Localidad: ")
    codigo_postal = input("Código Postal: ")
    provincia = input("Provincia: ")
    telefono_celular = input("Teléfono Celular: ")
    email = input("Email: ")
    rol = "alumno"

    
    clave = input("Ingrese su clave de acceso: ")
    confirmar_clave = input("Confirme su clave de acceso: ")

    if clave != confirmar_clave:
        print("Las claves no coinciden.")
        return


    usuario = {
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni,
        "direccion": direccion,
        "fecha_nacimiento": fecha_nacimiento,
        "localidad": localidad,
        "codigo_postal": codigo_postal,
        "provincia": provincia,
        "telefono_celular": telefono_celular,
        "email": email,
        "clave": clave,
        "rol": rol
    }

    print("Cuenta de usuario creada con éxito.")


crear_cuenta()


class UsuarioFinal:
    def __init__(self, nombre, apellido, dni, fecha_nacimiento, direccion, localidad, codigo_postal, provincia, telefono_celular, email, clave):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
        self.direccion = direccion
        self.localidad = localidad
        self.codigo_postal = codigo_postal
        self.provincia = provincia
        self.telefono_celular = telefono_celular
        self.email = email
        self.clave = clave
        self.estado = "Activo"
        self.curso= None
        
    def inscribirse_curso(self,curso):
        self.curso=curso
        
        


class Administrador:
    def __init__(self, nombre, apellido, dni, fecha_nacimiento, direccion, localidad, codigo_postal, provincia, telefono_celular, email, clave):
     self.nombre=nombre
     self.apellido=apellido
     self.dni=dni
     self.fecha_comienzo=fecha_nacimiento
     self.direccion=direccion
     self.localidad=localidad
     self.codigo_postal=codigo_postal
     self.provincia=provincia
     self.telefono_celular=telefono_celular
     self.email=email
     self.clave=clave
     
     
    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_apellido(self):
        return self.apellido

    def set_apellido(self, apellido):
        self.apellido = apellido

    def get_dni(self):
        return self.dni

    def set_dni(self, dni):
        self.dni = dni
        
    def get_direccion(self):
        return self.direccion
    
    def set_direccion(self,direccion):
        self.direccion=direccion
        
    def set_localidad(self):
        return self.localidad
    
    def get_localidad(self,localidad):
        self.localidad=localidad
        
    def get_codigo_postal(self):
        return self.codigo_postal
    
    def set_codigo_postal(self,codigo_postal):
        self.codigo_postal=codigo_postal
        
    def get_provincia(self):
        return self.provincia
    
    def set_provincia(self,provincia):
        self.provincia=provincia
        
    def get_telefono_celular(self):
        return self.telefono_celular
    
    def set_telefono_celular(self,telefono_celular):
        self.telefono_celular=telefono_celular
        
    def get_email(self):
        return self.email
    
    def set_email(self,email):
        self.email=email
        
    def get_clave(self):
        return self.clave
    
    def set_clave(self,clave):
        self.clave=clave
     
curso_ejemplo = Cursos("07/03/2024", "Curso de Python", "Aprende Python desde cero", "Objetivos del curso", "Programa del curso", 100, 3, "ruta_de_la_foto.jpg", "Activo")
curso_ejemplo = Cursos("14/03/2024", "Curso de Carpinteria", "Aprende Carpinteria desde cero", "Objetivos del curso", "Programa del curso", 100, 3, "ruta_de_la_foto.jpg", "Activo")
curso_ejemplo = Cursos("21/03/2024", "Curso de Tec.Reparador PC", "Aprende a reparar pc desde cero", "Objetivos del curso", "Programa del curso", 100, 3, "ruta_de_la_foto.jpg", "Activo")

usuario_final = UsuarioFinal("Juan", "González", " ", "05/06/1995", "Santiago", "Buenos Aires", "85787234", "Buenos Aires", "1188232384", "juangonzales@gmail.com", "password")
usuario_final.inscribirse_curso(curso_ejemplo)

administrador = Administrador("Admin", "Admin", " ", " ", " ", "Ciudad", " ", "Provincia", " ", "admin@gmail.com", "password")


class CarritoDeCompras:
    def __init__(self):
        self.items = []

    def agregar_curso(self, curso):
        self.items.append(curso)

    def calcular_total(self):
        return sum(curso.costo for curso in self.items)

class MedioDePago:
    def __init__(self, tipo):
        self.tipo = tipo

class TarjetaDeCreditoDebito(MedioDePago):
    def __init__(self, tipo, numero, titular):
        super().__init__(tipo)
        self.numero = numero
        self.titular = titular

class TransferenciaBancaria(MedioDePago):
    def __init__(self, tipo, banco, numero_cuenta):
        super().__init__(tipo)
        self.banco = banco
        self.numero_cuenta = numero_cuenta

class Compra:
    def __init__(self, carrito, medio_de_pago, usuario, fecha):
        self.carrito = carrito
        self.medio_de_pago = medio_de_pago
        self.usuario = usuario
        self.fecha = fecha
        self.monto_total = carrito.calcular_total()


curso1 = Cursos("07/03/2024", "Curso de Python", "Aprende Python desde cero", "Objetivos del curso", "Programa del curso", 100, 3, "ruta_de_la_foto.jpg", "Activo")
curso2 = Cursos("14/03/2024", "Curso de Carpinteria", "Aprende Carpinteria desde cero", "Objetivos del curso", "Programa del curso", 100, 3, "ruta_de_la_foto.jpg", "Activo")
curso3 = Cursos("21/03/2024", "Curso de Tec.Reparador PC", "Aprende a reparar pc desde cero", "Objetivos del curso", "Programa del curso", 100, 3, "ruta_de_la_foto.jpg", "Activo")

carrito = CarritoDeCompras()
carrito.agregar_curso(curso1)
carrito.agregar_curso(curso2)
carrito.agregar_curso(curso3)

tarjeta = TarjetaDeCreditoDebito("Tarjeta de Crédito", "1234 5678 9012 3456", "Fabian Godoy")
fecha_compra = "2023-09-12"
usuario = "Usuario"

compra = Compra(carrito, tarjeta, usuario, fecha_compra)

print("Resumen de la compra:")
for curso in compra.carrito.items:
 print(f"Curso: {curso.titulo}, Duración: {curso.duracion_meses}, Costo: ${curso.costo}")
 print(f"Total a pagar: ${compra.monto_total}")
 print(f"Medio de pago: {compra.medio_de_pago.tipo}")
 print(f"Fecha de compra: {compra.fecha}")
 print(f"Usuario: {compra.usuario}")
 
 
class Compra:
    def __init__(self, Id_Compra, Id_Carrito_Compra, Id_Medio_Pago, Id_Usuario, Fecha, Monto_Total):
        self.Id_Compra = Id_Compra
        self.Id_Carrito_Compra = Id_Carrito_Compra
        self.Id_Medio_Pago = Id_Medio_Pago
        self.Id_Usuario = Id_Usuario
        self.Fecha = Fecha
        self.Monto_Total = Monto_Total

    def __str__(self):
        return f"Compra ID: {self.Id_Compra}\nCarrito de Compra ID: {self.Id_Carrito_Compra}\nMedio de Pago ID: {self.Id_Medio_Pago}\nUsuario ID: {self.Id_Usuario}\nFecha: {self.Fecha}\nMonto Total: {self.Monton_Total}"

compra = Compra(12313132, 324234234, 3213213, 2313213, "2023-09-04", 312321321)

print(compra.Id_Compra)
print(compra.Fecha)

class MedioContacto:
    def __init__(self, id_medio_contacto, fecha, email, telefono, direccion, nombre):
        self.id_medio_contacto = id_medio_contacto
        self.fecha = fecha
        self.email = email
        self.telefono = telefono
        self.direccion = direccion
        self.nombre = nombre

    def __str__(self):
        return f"Medio de Contacto ID: {self.id_medio_contacto}\nFecha: {self.fecha}\nEmail: {self.email}\nTeléfono: {self.telefono}\nDirección: {self.direccion}\nNombre: {self.nombre}"

class TiposMedioContacto(MedioContacto):
    WHATSAPP = MedioContacto(1, "2023-09-04", "", "123-456-7890", "", "")
    CORREO_ELECTRONICO = MedioContacto(2, "2023-09-04", "ejemplo@email.com", "", "", "")
    CALL_CENTER = MedioContacto(3, "2023-09-04", "", "987-654-3210", "", "")
    REFERIDO_INTERNO = MedioContacto(4, "2023-09-04", "", "", "", "Referido Interno")

tipo_medio_contacto = TiposMedioContacto.WHATSAPP
print(tipo_medio_contacto.id_medio_contacto)

print(tipo_medio_contacto.telefono)
