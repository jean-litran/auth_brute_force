# Autenticação por força bruta

Este script Python utiliza a biblioteca Requests para fazer uma autenticação por força bruta em um endpoint de login especificado por uma URL. Ele faz uma requisição POST para a URL, utilizando uma lista de possíveis combinações de usuário e senha, carregadas a partir de um arquivo de texto. Se a autenticação for bem-sucedida, o script exibe a senha correta encontrada para o usuário.

## Requisitos

- Python 3.x
- Biblioteca Requests

## Como usar

1. Clone o repositório ou baixe o arquivo `auth_brute_force.py`
2. Abra o terminal e navegue até o diretório em que o arquivo está salvo
3. Execute o comando `python auth_brute_force.py`
4. Substitua a URL do endpoint de autenticação e o nome do arquivo de wordlist para atender às suas necessidades

## Observações

Este script é fornecido apenas para fins educacionais. Não é recomendado nem ético fazer uma autenticação por força bruta em um endpoint sem a permissão explícita do proprietário do site ou do sistema. A autenticação por força bruta pode ser ilegal e é considerada uma prática invasiva e mal-intencionada. Use este script com responsabilidade.
