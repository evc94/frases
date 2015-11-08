from django.db import models
from django.utils import timezone

class Frase(models.Model):
    autor = models.ForeignKey('auth.User')
    personaje = models.CharField(max_length=200)
    categoria = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(
            default=timezone.now)
    fecha_publicacion = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def borrar(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.texto
