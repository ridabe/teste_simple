# Use a imagem base do Python
FROM python:3.9

# Copie o arquivo requirements.txt para o contêiner
COPY requirements.txt .

# Instale as dependências a partir do arquivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copie todos os arquivos do diretório atual para o contêiner
COPY . .

# Exponha a porta onde o servidor está rodando
EXPOSE 8000

# Comando para rodar o servidor com Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
