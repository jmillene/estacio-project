# Usa uma imagem Python oficial
FROM python:3.9-slim

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia o arquivo requirements.txt e instala as dependências
COPY requirements.txt requirements.txt

# Instala as dependências, incluindo o psycopg2 e Flask
RUN pip install --no-cache-dir -r requirements.txt && \
    pip install psycopg2-binary flask

# Copia todo o código fonte para o contêiner
COPY . .

# Executa o aplicativo
CMD ["python", "app/app.py"]
