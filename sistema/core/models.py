from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    altura = models.IntegerField(default=0)
    peso = models.IntegerField(default=0)
    calorias = models.IntegerField(default=0)

    def __str__(self):
        return self.nome