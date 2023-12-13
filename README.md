
![Logo](https://simpleenergy.com.br/wp-content/uploads/2021/04/logo-1.png)


# Simpleenergy Teste

O desafio é desenvolver um programa em Python capaz de acessar e extrair informações de um website específico, organizando-as de forma eficaz.
Importante ressaltar que o uso do Selenium* ou bibliotecas similares** não é permitido.


## Etiquetas

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


## Resumo do sistema

Através desta Api, o sistema envia uma requisição para a url proposta no teste, recupera os links dentro do sistema, baixa os arquivos para a maquina local criando a pasta determinada no arquivo .env, complementando com subpastas
renomeadas com o codigo enviado. 

Salva os aqurivos neste diretório e em seguida executa a leitura do mesmo, trazendo as linhas contidas dentro de cada arquivo.
O sistema esta fechado para leitura apenas de PDF e TXT.

## Stack utilizada

**Back-end:** 
- Python

**Framework:** 
- FastApi

**Bibliotecas:**
- requests
- os
- PyPDF2
- BeautifulSoup
- dotenv


## Documentação da API

#### EndPoint de chamada

```http
  GET /api_url/files/{codigo}
  ```
#### Retorno da Api
```json
  {
    "pdf": [
        "e793ff53f0ca92f6205bc871546a2c79e54c4e0cd42c6a191e45e771d7217aca",
        "f60dacd4b776b6ab10d343a7129a0daf6a9ba23827854c99d9fdc3e1a1b846db"
    ],
    "txt": [
        "f60dacd4b776b6ab10d343a7129a0daf6a9ba23827854c99d9fdc3e1a1b846db.txt",
        "e793ff53f0ca92f6205bc871546a2c79e54c4e0cd42c6a191e45e771d7217aca.txt"
    ]
  }
  ```


## Variáveis de Ambiente

Para rodar esse projeto, você vai precisar adicionar as seguintes variáveis de ambiente no seu .env

`TEST_HOST`

`SAVE_DIR`


## Rodando via container

Clone o projeto

```bash
  git clone https://github.com/ridabe/teste_simple
```

Entre no diretório do projeto

```bash
  cd my-project
```

Para construir a imagem Docker a partir do Dockerfile, no terminal, navegue até o diretório onde está localizado o Dockerfile e execute o comando:

```bash
  docker build -t minha-api .
```

Para executar um contêiner com a imagem criada:

```bash
  docker run -p 8000:8000 minha-api
```

Utilize o postman ou outro app para acessar as rotas da api, acesse o endereço iniciado pelo servidor:

```bash
  http://127.0.0.1:8000/files/321465
```

## Rodando localmente

Clone o projeto

```bash
  git clone https://github.com/ridabe/teste_simple
```

Entre no diretório do projeto

```bash
  cd my-project
```

Inicie o servidor com o comando

```bash
  uvicorn main:app --reload
```

Utilize o postman ou outro app para acessar as rotas da api, acesse o endereço iniciado pelo servidor:

```bash
  http://127.0.0.1:8000/files/321465
```


## Melhorias Sugeridas

Melhorias propostas para a segunda versão:

- Refatorações
- Melhorias de performance
- Tratamento de erros(try)
- Testes Unitários
- criação do gitignore para nao enviar o .env
- Ajustes de Typo


## Suporte

Para suporte, mande um email para ridabe@uol.com.br ou entre em nosso whatsapp (11)94522-4263 (Ricardo Bene).


## Usado por

Esse projeto é parte do processo seletivo da:

- Simple Energy

![Logo](https://simpleenergy.com.br/wp-content/uploads/2021/04/logo-1.png)

