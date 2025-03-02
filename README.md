# Projeto de Catálogo de Filmes

Este é um projeto Django que gerencia um catálogo de filmes, diretores e atores. Ele inclui funcionalidades CRUD (Create, Read, Update, Delete) para filmes, diretores e atores, além de integração com a API do OMDB para buscar informações de filmes.

## Funcionalidades

- **CRUD para Diretores**: Crie, liste, atualize e delete diretores.
- **CRUD para Atores**: Crie, liste, atualize e delete atores.
- **CRUD para Filmes**: Crie, liste, atualize e delete filmes.
- **Busca de Filmes por ID**: Busque informações de filmes usando o ID do IMDb.
- **Integração com a API do OMDB**: Consuma a API do OMDB para obter detalhes de filmes.

## Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- Docker
- Docker Compose

## Instalação com Docker

Siga os passos abaixo para configurar e executar o projeto usando Docker.

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
2. Configure o ambiente
O projeto já está configurado para rodar com Docker. Basta executar o docker-compose para subir os serviços.

3. Suba os containers
Execute o seguinte comando para construir e iniciar os containers:

bash
Copy
docker-compose up --build
Isso irá:

Construir a imagem do Django com base no Dockerfile.

Configurar o banco de dados MySQL.

Executar o servidor Django na porta 8000.

4. Acesse o projeto
Django: Acesse http://localhost:8000/ no navegador.

Admin: Acesse http://localhost:8000/admin/ para o painel de administração.

5. Aplique as migrações
Para criar as tabelas no banco de dados, execute as migrações dentro do container:

bash
Copy
docker-compose exec web python manage.py migrate
6. Crie um superusuário (opcional)
Para acessar o painel de administração, crie um superusuário:

bash
Copy
docker-compose exec web python manage.py createsuperuser
Estrutura do Projeto
Copy
filmes/
├── catalogo/
│   ├── migrations/       # Migrações do banco de dados
│   ├── templates/        # Templates HTML
│   ├── admin.py          # Configuração do Django Admin
│   ├── apps.py           # Configuração do app
│   ├── models.py         # Modelos do banco de dados
│   ├── serializers.py    # Serializadores para a API
│   ├── urls.py           # Rotas do app
│   ├── utils.py          # Funções utilitárias (ex: buscar_filme_omdb)
│   └── views.py          # Views do app
├── filmes/
│   ├── settings.py       # Configurações do projeto
│   ├── urls.py           # Rotas principais do projeto
│   └── wsgi.py           # Configuração WSGI
├── manage.py             # Script de gerenciamento do Django
├── Dockerfile            # Configuração do container Django
├── docker-compose.yml    # Configuração dos serviços Docker
└── requirements.txt      # Lista de dependências
Dependências
O projeto utiliza as seguintes dependências, listadas no arquivo requirements.txt:

Django: Framework web.

djangorestframework: Para criar APIs RESTful.

mysqlclient: Conector para o banco de dados MySQL.

requests: Para consumir a API do OMDB.

plaintext
Copy
asgiref==3.8.1
certifi==2025.1.31
charset-normalizer==3.4.1
Django==5.1.6
djangorestframework==3.15.2
idna==3.10
mysqlclient==2.2.7
requests==2.32.3
sqlparse==0.5.3
tzdata==2025.1
urllib3==2.3.0
Como Usar
1. Acesse o Painel de Administração
URL: http://localhost:8000/admin/

Use as credenciais do superusuário para fazer login.

2. Rotas da API
Listar Diretores: GET /api/diretores/

Detalhes de um Diretor: GET /api/diretores/<int:pk>/

Listar Atores: GET /api/atores/

Detalhes de um Ator: GET /api/atores/<int:pk>/

Listar Filmes: GET /api/filmes/

Detalhes de um Filme: GET /api/filmes/<int:pk>/

Buscar Filme por ID: POST /api/buscar-filme-por-id/

3. Buscar Filme por ID
Acesse a página de busca por ID: http://localhost:8000/buscar-filme-por-id/.

Insira o ID do filme (ex: tt3896198 para "Guardians of the Galaxy Vol. 2").

Clique em "Buscar" para ver os detalhes do filme.

Contribuição
Contribuições são bem-vindas! Siga os passos abaixo:

Faça um fork do projeto.

Crie uma branch para sua feature (git checkout -b feature/nova-feature).

Commit suas mudanças (git commit -m 'Adiciona nova feature').

Faça push para a branch (git push origin feature/nova-feature).

Abra um Pull Request.

Licença
Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

Contato
Se tiver dúvidas ou sugestões, entre em contato:

Nome: Gabriel Castro

E-mail: gabriel.castro@gmail.com

GitHub: DevBielCastro

Copy

---

### **Como Usar o README.md**

1. Crie um arquivo chamado `README.md` na raiz do seu projeto.
2. Copie e cole o conteúdo acima no arquivo.
3. Personalize as informações, como o nome do repositório, contato e descrição do projeto.