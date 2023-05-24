from django.db import models


class Contacto(models.Model):
    __nombre = models.CharField(max_length=50)
    __apellido = models.CharField(max_length=50)
    __telefono = models.CharField(max_length=9)
    __email = models.EmailField()
    __password = models.CharField(max_length=50)
    __dni = models.CharField(max_length=9)

    # geters
    def get_nombre(self):
        return self.__nombre
    def get_apellido(self):
        return self.__apellido
    def get_telefono(self):
        return self.__telefono
    def get_email(self):
        return self.__email
    def get_password(self):
        return self.__password
    def get_dni(self):
        return self.__dni
    
    def nombre_completo(self):
        return self.nombre + ' ' + self.apellido
    
    def reestablecer_password(self, nueva_password):
        self.__password = nueva_password
        self.save()
