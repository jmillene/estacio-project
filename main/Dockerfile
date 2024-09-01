# Usar uma imagem Python oficial
FROM python:3.9-slim

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia o arquivo requirements.txt e instalar as dependências
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código fonte para o contêiner
COPY . .

# Executa o aplicativo
CMD ["python", "app.py"]
