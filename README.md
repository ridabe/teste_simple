
![Logo](https://simpleenergy.com.br/wp-content/uploads/2021/04/logo-1.png)


# Simpleenergy Teste

O desafio é desenvolver um programa em Python capaz de acessar e extrair informações de um website específico, organizando-as de forma eficaz.
Importante ressaltar que o uso do Selenium* ou bibliotecas similares** não é permitido.




## Etiquetas

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


## Stack utilizada

**Back-end:** Python

**Bibliotecas:** FastApi, requests, os, PyPDF2, BeautifulSoup, dotenv


## Documentação da API

#### Retorna todos os itens

```http
  GET /api_url/files/{codigo}```



## Variáveis de Ambiente

Para rodar esse projeto, você vai precisar adicionar as seguintes variáveis de ambiente no seu .env

`TEST_HOST`

`SAVE_DIR`


## Rodando localmente

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


## Melhorias Sugeridas

Melhorias propostas para a segunda versão:
Refatorações, melhorias de performance, tratamento de erros(try), Testes Unitários.


## Suporte

Para suporte, mande um email para ridabe@uol.com.br ou entre em nosso whatsapp (11)94522-4263 (Ricardo Bene).


## Usado por

Esse projeto é parte do processo seletivo da:

- Simple Energy

