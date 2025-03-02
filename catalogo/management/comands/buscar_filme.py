from django.core.management.base import BaseCommand
from catalogo.models import Filme, Diretor, Ator
from catalogo.utils import buscar_filme_omdb
from django.conf import settings

class Command(BaseCommand):
    help = 'Busca um filme na API do OMDB e salva no banco de dados.'

    def add_arguments(self, parser):
        parser.add_argument('titulo', type=str, help='Título do filme a ser buscado.')

    def handle(self, *args, **kwargs):
        titulo = kwargs['titulo']
        api_key = settings.OMDB_API_KEY

        # Busca o filme na API do OMDB
        dados_filme = buscar_filme_omdb(titulo)

        if dados_filme:
            # Cria ou atualiza o filme no banco de dados
            diretor, _ = Diretor.objects.get_or_create(nome=dados_filme.get('Director', 'Desconhecido'))
            filme, created = Filme.objects.get_or_create(
                titulo=dados_filme['Title'],
                defaults={
                    'ano': int(dados_filme.get('Year', '0')[:4]),  # Pega apenas o ano
                    'diretor': diretor,
                    'poster': dados_filme.get('Poster', ''),
                    'sinopse': dados_filme.get('Plot', ''),
                }
            )

            # Adiciona os atores
            atores = dados_filme.get('Actors', '').split(', ')
            for nome_ator in atores:
                ator, _ = Ator.objects.get_or_create(nome=nome_ator)
                filme.atores.add(ator)

            if created:
                self.stdout.write(self.style.SUCCESS(f'Filme "{filme.titulo}" salvo com sucesso!'))
            else:
                self.stdout.write(self.style.WARNING(f'Filme "{filme.titulo}" já existe no banco de dados.'))
        else:
            self.stdout.write(self.style.ERROR(f'Filme "{titulo}" não encontrado.'))