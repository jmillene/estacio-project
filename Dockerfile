# Usa uma imagem base Python
FROM python:3.9-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia o arquivo requirements.txt e instala as dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código fonte para o diretório de trabalho
COPY . .

# Define a variável de ambiente PYTHONPATH
ENV PYTHONPATH=/app

# Comando para iniciar a aplicação
CMD ["python", "app/server.py"]
