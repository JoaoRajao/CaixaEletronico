
# CaixaEletronico

Este repositório contém o código-fonte de uma API de Caixa Eletrônico que simula o processo de saques em cédulas com o menor número de notas possíveis.

## Estrutura do Projeto

O projeto está dividido nas seguintes pastas principais:

- `controladores`: Contém os controladores que lidam com as requisições HTTP.
- `modelos`: Inclui os modelos de negócio, como a lógica de saque.
- `testes`: Armazena os testes unitários da aplicação.
- `docs`: Diretório para documentação do projeto gerada pelo Sphinx.

## Configuração do Ambiente

Para configurar o ambiente necessário para executar este projeto, você deve seguir os passos abaixo.

### Pré-requisitos

Antes de iniciar, garanta que você tem o Python instalado em sua máquina. Este projeto foi desenvolvido usando Python 3.8.

### Instalação

1. Clone o repositório para sua máquina local:
   ```bash
   git clone https://seu-repositorio/CaixaEletronico.git
   cd CaixaEletronico

2. Instale as dependências do projeto:
   pip install -r requisitos.txt


### Executando a Aplicação
Para executar a aplicação, use o seguinte comando no diretório raiz do projeto:
    python aplicacao.py

### Testando a Aplicação
Os testes foram escritos usando o framework unittest do Python. Para executar os testes, siga estes passos:

python -m unittest discover -s testes
