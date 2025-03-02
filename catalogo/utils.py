import requests
from django.conf import settings

def buscar_filme_omdb(titulo):
    """
    Busca os dados de um filme na API do OMDB usando o título.
    :param titulo: Título do filme a ser buscado.
    :return: Dados do filme em formato JSON ou None se não encontrar.
    """
    api_key = settings.OMDB_API_KEY
    url = f"http://www.omdbapi.com/?t={titulo}&apikey={api_key}"
    response = requests.get(url)
    print("URL da requisição:", url)  # Depuração
    print("Status Code:", response.status_code)  # Depuração
    print("Resposta da API:", response.json())  # Depuração
    if response.status_code == 200:
        dados = response.json()
        if dados.get("Response") == "True":
            return dados
    return None

def buscar_filme_por_id(imdb_id):
    """
    Busca os dados de um filme na API do OMDB usando o ID do IMDb.
    :param imdb_id: ID do filme no IMDb (ex: tt3896198).
    :return: Dados do filme em formato JSON ou None se não encontrar.
    """
    api_key = settings.OMDB_API_KEY
    url = f"http://www.omdbapi.com/?i={imdb_id}&apikey={api_key}"
    response = requests.get(url)
    print("URL da requisição:", url)  # Depuração
    print("Status Code:", response.status_code)  # Depuração
    print("Resposta da API:", response.json())  # Depuração
    if response.status_code == 200:
        dados = response.json()
        if dados.get("Response") == "True":
            return dados
    return None