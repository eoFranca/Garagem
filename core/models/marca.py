from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=50)
    nacionalidade = models.CharField(max_length=100,blank = True,null = True)
    

    def __str__(self):
            return f"{self.nome.ToUpperCase()} {self.nacionalidade}"