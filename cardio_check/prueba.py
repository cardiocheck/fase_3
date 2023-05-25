# FALTA PODER IMPRIMIR LOS DATOS DE LA BASE DE DATOS


from formulario.models import Contacto

registros = Contacto.objects.all()

for registro in registros:
    nombre = registro.nombre
    print('nombre: ', nombre)

    apellido = registro.apellido
    print('apellido: ', apellido)

    email = registro.email
    print('email: ', email)

    telefono = registro.telefono    
    print('telefono: ', telefono)

    password = registro.password
    print('contraseña: ', password)

    dni = registro.dni
    print('dni: ', dni)
