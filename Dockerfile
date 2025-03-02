FROM python:3.11.9-slim

RUN apt-get update && \
    apt-get install -y \
    pkg-config \
    libmariadb-dev-compat \
    gcc \
    python3-dev \
    libmariadb-dev && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

# Precisei adicionar este RUN pois estava enfrentando erros ao tentar dockerizar o projeto
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
