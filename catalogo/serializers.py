from rest_framework import serializers
from .models import Diretor, Ator, Filme

class DiretorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diretor
        fields = '__all__'  

class AtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ator
        fields = '__all__'  

class FilmeSerializer(serializers.ModelSerializer):
    diretor = DiretorSerializer(read_only=True)  
    atores = AtorSerializer(many=True, read_only=True)  

    class Meta:
        model = Filme
        fields = '__all__'  # Esou usando essa função pois ela Inclui todos os campos do modelo, assim como usado em diretor e ator