import requests
import os
import PyPDF2
from bs4 import BeautifulSoup
from dotenv import dotenv_values
from fastapi import FastAPI

app = FastAPI()

env_vars = dotenv_values(".env")

url = env_vars.get("TEST_HOST")
save_dir = env_vars.get("SAVE_DIR")


@app.get("/files/{codigo}")
def get_item(codigo: int):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/87.0.4280.88 Safari/537.36",
        'Accept': '*/*'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Utiliza BeautifulSoup para analisar o conteúdo da página
        soup = BeautifulSoup(response.content, 'html.parser')

        # Encontra o token CSRF
        token_csrf = None

        # Procura o token CSRF em um input com name='csrf'
        input_csrf = soup.find('input', {'name': 'csrf'})
        if input_csrf:
            token_csrf = input_csrf.get('value')

        # Se o token CSRF foi encontrado
        if token_csrf:
            # Definição do payload com o código de acesso e o token CSRF
            payload = {
                'codigo': codigo,
                'csrf': token_csrf  # Adicione o token CSRF ao payload
            }

            # Definição dos novos cabeçalhos
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/87.0.4280.88 Safari/537.36",
                'Accept': '*/*'
            }

            # Realiza uma requisição POST com o payload e cabeçalhos definidos
            response_post = requests.post(url, data=payload, headers=headers)

            if response_post.status_code == 200:
                soup_post = BeautifulSoup(response_post.content, 'html.parser')

                # Extrai dados do HTML usando as funções do BeautifulSoup
                # Por exemplo, encontrar todos os links na página
                links = soup_post.find_all('a')
            else:
                return f'Falha na requisição POST. {response_post.status_code}'

            if not os.path.exists(save_dir):
                os.makedirs(save_dir)
            # Exibir os links encontrados
            for link in links:
                href = link.get('href')
                if href.endswith('.pdf') or href.endswith('.txt'):
                    # Realiza uma requisição GET para baixar o arquivo
                    href = url + href
                    file_response = requests.get(href, headers=headers)

                    if file_response.status_code == 200:
                        # Extrai o nome do arquivo do link
                        get_name = href.split('/')[-1]
                        get_code = get_name.split('-')
                        get_code = get_code[1].split('.')
                        new_dir = save_dir + "/" + get_code[0]
                        if not os.path.exists(new_dir):
                            os.makedirs(new_dir)
                        filename = os.path.join(new_dir, href.split('/')[-1])
                        # Salva o conteúdo do arquivo
                        with open(filename, 'wb') as file:
                            file.write(file_response.content)
                        # print(f'Arquivo {filename} baixado com sucesso.')

                        response = read_item(new_dir)

                    else:
                        print(f'Falha ao baixar o arquivo do link {href}')
        else:
            return 'Token CSRF não encontrado.'

    else:
        return 'Falha ao acessar o site.'

    return response


def read_item(save_dir):
    conteudo_pdf = []
    conteudo_txt = []
    # Percorre os arquivos baixados no diretório
    for filename in os.listdir(save_dir):
        if filename.endswith('.pdf'):
            files_dir = save_dir + '/' + filename
            with open(files_dir, 'rb') as file:
                # Cria um objeto PDFReader
                pdf_reader = PyPDF2.PdfReader(file)

                # Extrai o texto de cada página do PDF
                num_pages = len(pdf_reader.pages)
                for page_num in range(num_pages):
                    page = pdf_reader.pages[page_num]
                    text = page.extract_text()

                    # Exibe o texto extraído
                    conteudo_pdf.append(text)

        if filename.endswith('.txt'):
            files_dir = save_dir + '/' + filename
            with open(files_dir, 'r') as file:
                lines = file.readlines()
                # Lê cada linha do arquivo e exibe
                for line in lines:
                    conteudo_txt.append(line.strip())  # strip() remove espaços em branco extras e quebras de linha
    return {
        "pdf": conteudo_pdf,
        "txt": conteudo_txt
    }
