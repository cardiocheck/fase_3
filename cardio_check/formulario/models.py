from django.db import models


class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=9)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    dni = models.CharField(max_length=9)
    
    def nombre_completo(self):
        return self.nombre + ' ' + self.apellido
    
    def reestablecer_password(self, nueva_password):
        self.__password = nueva_password
        self.save()
