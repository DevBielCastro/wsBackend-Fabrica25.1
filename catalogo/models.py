from django.db import models

class Diretor(models.Model):
    nome = models.CharField(max_length=100, unique=True)  # Fiz assim para evitar duplicidades (pois passeis horas resolvendo problemas da forma inicial que fiz)

    def __str__(self):
        return self.nome  # Representação

class Ator(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome  

class Filme(models.Model):
    titulo = models.CharField(max_length=200)
    ano = models.IntegerField()
    diretor = models.ForeignKey(Diretor, on_delete=models.SET_NULL, null=True, related_name='filmes') 
    atores = models.ManyToManyField(Ator, related_name='filmes')
    poster = models.URLField(null=True, blank=True)  
    sinopse = models.TextField(null=True, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return self.titulo