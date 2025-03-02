from rest_framework import generics
from django.shortcuts import render
from django.conf import settings
from .models import Diretor, Ator, Filme
from .serializers import DiretorSerializer, AtorSerializer, FilmeSerializer
from .utils import buscar_filme_por_id


class DiretorList(generics.ListCreateAPIView):
    queryset = Diretor.objects.all()
    serializer_class = DiretorSerializer

class DiretorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Diretor.objects.all()
    serializer_class = DiretorSerializer


class AtorList(generics.ListCreateAPIView):
    queryset = Ator.objects.all()
    serializer_class = AtorSerializer

class AtorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ator.objects.all()
    serializer_class = AtorSerializer


class FilmeList(generics.ListCreateAPIView):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer

class FilmeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer

def buscar_filme_por_id_view(request):
    """
    View para buscar um filme por ID no IMDb.
    """
    if request.method == 'POST':
        imdb_id = request.POST.get('imdb_id')  
        dados_filme = buscar_filme_por_id(imdb_id) 

        if dados_filme:
            mensagem = f'Filme "{dados_filme["Title"]}" encontrado!'
        else:
            mensagem = f'Filme com ID "{imdb_id}" não encontrado.'

        return render(request, 'catalogo/buscar_filme.html', {'mensagem': mensagem, 'dados_filme': dados_filme})

    return render(request, 'catalogo/buscar_filme.html')