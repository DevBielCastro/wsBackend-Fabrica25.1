from django.urls import path
from .views import (
    DiretorList, DiretorDetail,  
    AtorList, AtorDetail,        
    FilmeList, FilmeDetail,      
    buscar_filme_por_id_view     
)

urlpatterns = [
    path('diretores/', DiretorList.as_view(), name='diretor-list'),
    path('diretores/<int:pk>/', DiretorDetail.as_view(), name='diretor-detail'),
    path('atores/', AtorList.as_view(), name='ator-list'),
    path('atores/<int:pk>/', AtorDetail.as_view(), name='ator-detail'),
    path('filmes/', FilmeList.as_view(), name='filme-list'),
    path('filmes/<int:pk>/', FilmeDetail.as_view(), name='filme-detail'),
    path('buscar-filme-por-id/', buscar_filme_por_id_view, name='buscar-filme-por-id'),
]